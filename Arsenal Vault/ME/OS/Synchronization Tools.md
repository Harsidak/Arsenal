# 🔄 Synchronization Tools

> [!NOTE] Source Context
> This note covers operating system synchronization tools, concepts, and algorithms based on **[[BOOK - OPERATING SYSTEM CONCEPTS (Silberschatz, Galvin & Gagne)]]** by Silberschatz, Galvin, and Gagne.
> **Parent Topic**: [[OS]]

---

## 📌 Introduction to Synchronization

When multiple threads or processes access and manipulate shared data concurrently, the outcome of the execution depends on the particular order in which the access takes place. This scenario is called a **[[Race Condition]]**. To prevent race conditions and ensure data consistency, the operating system provides various **Synchronization Tools**.

These tools help manage the **Critical Section Problem**, where cooperative processes must coordinate their execution to ensure that no two processes execute their critical sections (where shared data is accessed/modified) at the same time.

---

## 🛠️ Key Concepts & Tools We Will Cover

As we proceed with our study, we will expand this index with deep dives into:

1. **[[Critical Section Problem]]**
   - Mutual Exclusion (Mutex)
   - Progress
   - Bounded Waiting
   - **[[Peterson's Solution]]** (Classic software-based two-process approach)
2. **[[Hardware-based Synchronization]]**
   - Memory Models (Strongly vs. Weakly Ordered)
   - Memory Barriers & Fences
   - **[[Hardware Instructions]]** (TestAndSet, CompareAndSwap)
3. **Mutex Locks**
   - Spinlocks vs. Sleep-locks
4. **Semaphores**
   - Counting vs. Binary Semaphores
5. **Monitors**
   - Condition Variables
6. **Liveness Hazards**
   - Deadlocks and Starvation

---

## 🗂️ Related Notes & Subtopics
* [[Race Condition]] - Detailed analysis of race conditions with assembly interleaving traces and real-world failure scenarios.
* [[Critical Section Problem]] - Explains the four process sections (entry, critical, exit, remainder), the three requirements for solutions, and preemptive vs. non-preemptive OS kernels.
* [[Peterson's Solution]] - A classic software-based two-process synchronization algorithm, its mathematical proofs of correctness, and why it fails on modern reordering hardware.
* [[Hardware-based Synchronization]] - Covers memory models (strongly vs. weakly ordered), instruction reordering, and how memory barriers (fences) guarantee thread coordination.
* [[Hardware Instructions]] - Explains low-level atomic operations (TestAndSet and CompareAndSwap), C pseudo-code models, mutual exclusion loops, and CPU bus locking.
