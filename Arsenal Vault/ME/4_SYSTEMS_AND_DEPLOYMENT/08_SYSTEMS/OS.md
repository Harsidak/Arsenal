# 🖥️ Operating Systems (OS)

> [!NOTE] Source Context
> Fundamental concepts of low-level systems, hardware management, and process concurrency are learned from the seminal resource [[BOOK - OPERATING SYSTEM CONCEPTS (Silberschatz, Galvin & Gagne)]].

---

## 🗺️ Key Operating System Topics

### 1. Process Concurrency & Multi-threading
*   Understanding how the CPU executes isolated **Processes** and shared-memory **Threads**.
*   **Race Conditions & Mutual Exclusion**: Synchronizing threads using Mutexes and Semaphores to prevent memory corruption. (See: [[Synchronization Tools]])

### 2. Memory & Virtualization
*   How the OS virtualizes raw hardware RAM into protected address spaces via **Paging** and **Virtual Memory**.
*   Preventing memory leaks, heap/stack overflows, and disk thrashing.

### 3. CPU Scheduling & Kernel Architecture
*   How the kernel schedules code execution across multi-core systems (Round Robin, Multilevel Queue schedulers).
*   User Space vs. Kernel Space and the role of **System Calls**.

---

**Related Notes**:
*   [[BOOK - COMPUTER ARCHITECTURE (Hennessy & Patterson)]] (Low-level hardware design)
* [[Synchronization Tools]]
