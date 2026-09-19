# ⚡ Hardware Instructions

> [!NOTE] Context & References
> **Parent Note**: [[Synchronization Tools]]
> **Partner Concept**: [[Hardware-based Synchronization]]
> **Theoretical Source**: [[BOOK - OPERATING SYSTEM CONCEPTS (Silberschatz, Galvin & Gagne)]]
> **Prerequisite**: [[Critical Section Problem]]

---

## 📌 Introduction to Atomic Hardware Instructions

**Hardware Instructions** are special low-level operations provided directly by modern CPU architectures that perform complex tasks—such as testing and modifying a word, or swapping the contents of two words—**atomically** (meaning they execute as a single, uninterruptible unit of work).

### ❓ Why We Need Them
Purely **software-based solutions** to synchronization (like [[Peterson's Solution]]) are no longer guaranteed to work on modern multi-core computers. To improve execution speeds, modern compilers and CPU pipelines frequently reorder memory read and write operations. 

By using hardware-level atomic instructions, the system guarantees that the instructions:
1. Cannot be interrupted mid-execution.
2. Cannot be interleaved with other memory accesses from other cores.
3. Will execute sequentially in a system-defined, arbitrated order.

---

## 🔑 1. The `test_and_set()` Instruction

The `test_and_set()` instruction is a hardware-supported operation that allows a processor core to test and modify the content of a memory word atomically.

### 💻 Logical C Equivalence
Although implemented in hardware gates, its logical behavior is equivalent to the following C function:

```c
boolean test_and_set(boolean *target) {
    boolean rv = *target;  // Save the original value
    *target = true;        // Unconditionally set the value to true
    return rv;             // Return the original saved value
}
```

### 🛡️ Mutual Exclusion Implementation
We can use a shared boolean variable `lock` (initialized to `false`) to protect critical sections:

```c
do {
    // Spin/busy-wait while another process holds the lock
    while (test_and_set(&lock))
        ; /* busy wait - do nothing */

    /* ----- CRITICAL SECTION ----- */
    // Safely read or modify shared resources
    
    /* ------ EXIT SECTION ------ */
    lock = false;          // Release the lock

    /* ---- REMAINDER SECTION ---- */
    // Execute independent local computations
} while (true);
```

#### ⚙️ Mechanics:
* **Acquiring the lock:** The first process to call `test_and_set(&lock)` finds `lock` is `false`. The instruction returns `false` (breaking the `while` loop) and atomically overwrites `lock` to `true`.
* **Busy waiting:** Any subsequent process calling `test_and_set(&lock)` finds `lock` is `true`. The instruction returns `true` and maintains the state as `true`, forcing the process to spin in the `while` loop.
* **Releasing the lock:** The process exits the critical section and sets `lock = false`, immediately freeing the lock.

---

## 🔑 2. The `compare_and_swap()` (CAS) Instruction

The `compare_and_swap()` (often abbreviated as **CAS**) instruction operates on integer words atomically. Rather than unconditionally setting a value, CAS performs a **conditional swap**.

### 💻 Logical C Equivalence
Its logical behavior is equivalent to the following C function:

```c
int compare_and_swap(int *value, int expected, int new_value) {
    int temp = *value;         // Save the original value
    if (*value == expected) {  // Only swap if the value matches what we expect
        *value = new_value;
    }
    return temp;               // Always return the original saved value
}
```

### 🛡️ Mutual Exclusion Implementation
We declare a shared integer `lock` initialized to `0` (where `0` = available, `1` = locked):

```c
while (true) {
    // Spin/busy-wait until compare_and_swap successfully swaps 0 to 1
    while (compare_and_swap(&lock, 0, 1) != 0)
        ; /* busy wait - do nothing */
        
    /* ----- CRITICAL SECTION ----- */
    // Safely read or modify shared resources
    
    /* ------ EXIT SECTION ------ */
    lock = 0;                  // Release the lock by setting it back to 0
    
    /* ---- REMAINDER SECTION ---- */
}
```

#### ⚙️ Mechanics:
* **Acquiring the lock:** When `lock == 0`, a call to `compare_and_swap(&lock, 0, 1)` compares the lock against `expected` (`0`). Since they match, it sets `lock = 1` and returns the original value `0` (breaking the loop).
* **Busy waiting:** When `lock == 1`, CAS finds `lock != expected (0)`. It leaves the lock as `1` and returns `1`. The calling process continues to spin.
* **Releasing the lock:** The lock holder sets `lock = 0`.

---

## ⚖️ Comparison: `test_and_set()` vs. `compare_and_swap()`

While both are low-level atomic hardware instructions used to achieve mutual exclusion, they have fundamentally different signatures, capabilities, and use-cases:

| Feature             | `test_and_set()`                                          | `compare_and_swap()` (CAS)                                                  |
| :------------------ | :-------------------------------------------------------- | :-------------------------------------------------------------------------- |
| **Operation Type**  | **Unconditional write**: Always sets target to `true`.    | **Conditional write**: Only writes if the current value matches `expected`. |
| **Input Arguments** | 1 argument (Pointer to a boolean: `&lock`).               | 3 arguments (Pointer, `expected_value`, `new_value`).                       |
| **Data Types**      | Operates strictly on **booleans**.                        | Operates on **integers, pointers, and memory words**.                       |
| **Key Output**      | Returns the **original boolean state** of the target.     | Returns the **original value** (regardless of swap success).                |
| **Versatility**     | 🔴 Low: Only suitable for basic binary locks (spinlocks). | 🟢 High: Suitable for complex, **lock-free** data structures.               |
|                     |                                                           |                                                                             |
spinlock: A spinlock is ==a low-level synchronization lock where a thread waiting to access shared data continuously loops—or "spins"—in a busy-wait state until the lock becomes available==.
### 🔍 Key Differences Explained

1. **Conditional vs. Unconditional Write**
   - `test_and_set()` performs an **unconditional write**. It blindly forces the target memory location to `true`. Its only "check" is returning the *prior* state.
   - `compare_and_swap()` performs a **conditional write**. It executes a write *only if* the target memory matches a specified filter (`expected`). This conditional aspect makes it significantly safer and more powerful.

2. **Types of Locks & Data Structures**
   - **Simple Spinlocks:** `test_and_set()` is perfectly tailored for a simple binary lock variable. It's lightweight and efficient for simple toggle flags.
   - **Lock-Free Programming (Optimistic Concurrency Control):** CAS is the foundational building block for lock-free data structures (like lock-free stacks, queues, and atomic counters). For example, a thread can read a value, perform calculations, and write it back *only if* no other thread changed it while the calculation was occurring:
     ```c
     do {
         old_val = shared_counter;
         new_val = old_val + 1;
     } while (compare_and_swap(&shared_counter, old_val, new_val) != old_val);
     ```
     This allows high-concurrency systems to avoid thread-blocking entirely.

---

## ⚠️ Limitations & Real-world Implementation

### 1. The Bounded-Waiting Problem (Starvation)
While both simple loops enforce *Mutual Exclusion* and *Progress*, **they do not guarantee Bounded Waiting**. When multiple processes are spinning, the lock is allocated arbitrarily when released. A slow process could theoretically be starved forever while faster processes repeatedly cycle in and out of the lock.
* *OS Solution*: Production-grade mutexes use CAS inside more complex data structures containing wait-queues to guarantee fair scheduling.

### 2. CPU Overhead (Busy-Waiting)
Spinning in a `while` loop consumes 100% of a CPU core's cycles, generating heat and wasting energy. Spinlocks are only efficient if the critical section is extremely short.

### 3. Intel x86 Hardware Implementation
On Intel x86 architectures, the CAS operation is implemented using the **`cmpxchg`** assembly instruction. In multiprocessor environments, it is prefixed with **`lock`** (e.g., `lock cmpxchg`), which locks the system bus or cache lines to prevent other cores from reading or writing the target address mid-operation.
