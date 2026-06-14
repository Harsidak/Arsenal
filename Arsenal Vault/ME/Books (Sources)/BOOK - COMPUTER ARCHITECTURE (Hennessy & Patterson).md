# 📘 Book - Computer Architecture: A Quantitative Approach

> [!NOTE] Authors
> **John L. Hennessy and David A. Patterson** (The legendary textbook on modern CPU/GPU microarchitecture design)
> **Links**: [[OS]]

---

## 🧠 Simpler Breakdown of Computer Architecture

### 1. The Quantitative Principles of Design
*   **The Simple Idea**: Computer architecture is no longer just art; it is a quantitative science measured by performance, power, and cost.
*   **Amdahl's Law**: Tells you how much speedup you get by upgrading a *specific* component of your system:
    $$\text{Speedup}_{\text{overall}} = \frac{1}{(1 - F) + \frac{F}{S}}$$
    *(Where $F$ is the fraction of computation enhanced, and $S$ is the speedup of that fraction).*
    *   **ELI5**: If your program spends 90% of its time doing math and 10% loading files, doubling your file loading speed ($S=2$ for 10%) barely does anything. You must focus on optimizing the bottleneck (the 90%).
*   **Locality of Reference**:
    *   **Temporal Locality**: If your code accesses memory address $X$, it will likely access $X$ again very soon (e.g., inside a loop).
    *   **Spatial Locality**: If your code accesses memory address $X$, it will likely access $X+1$ or $X+2$ very soon (e.g., reading an array).

### 2. Instruction Set Architecture (ISA) & RISC vs. CISC
*   **The Simple Idea**: The ISA is the contract between the hardware and the software—the dictionary of instructions the CPU understands.
*   **RISC (Reduced Instruction Set Computer)**: Simple, fixed-length instructions executed in a single clock cycle (e.g., ARM, RISC-V). Focuses on efficient hardware.
*   **CISC (Complex Instruction Set Computer)**: Rich, variable-length instructions that perform complex operations in multiple cycles (e.g., x86). Focuses on compiler simplicity.
*   **Why it matters**: Almost all modern mobile chips and Apple Silicon are RISC (ARM) because it achieves much higher energy efficiency.

### 3. Pipelining & Instruction-Level Parallelism (ILP)
*   **The Simple Idea**: Pipelining is like an assembly line for instructions. Instead of waiting for one instruction to finish completely before starting the next, the CPU overlaps their execution.
*   **The Hazards (Bugs in the Assembly Line)**:
    *   **Structural Hazard**: Two instructions need the same hardware resource at the same time.
    *   **Data Hazard**: Instruction B needs the output of Instruction A, but Instruction A hasn't calculated it yet (requires *Forwarding* or *Stalling*).
    *   **Control Hazard**: The CPU doesn't know which instruction is next because of a conditional branch (requires *Branch Prediction*).
*   **Out-of-Order Execution**: Modern CPUs dynamically reschedule instructions on the fly (using Tomasulo's algorithm) to keep the execution units busy even if one instruction is stalled waiting for memory.

### 4. Memory Hierarchy & Caches
*   **The Simple Idea**: CPUs are incredibly fast, but RAM is incredibly slow (known as the "Memory Wall"). To bridge this gap, we use small, lightning-fast SRAM memories called **Caches** (L1, L2, L3).
*   **Cache Coherence**: In multi-core processors, each core has its own private L1 cache. If Core 1 modifies variable $X$, Core 2's L1 cache must be updated or invalidated immediately to prevent reading stale data. This is managed by snooping protocols like **MESI**.

### 5. Data-Level Parallelism: Vector Chips & GPUs
*   **The Simple Idea**: Instead of building one massive, complex core to run single instructions (SISD), we can build thousands of tiny, simple cores that execute the *same instruction* on *different streams of data* simultaneously (SIMD/SIMT).
*   **Why it matters**: This is the exact architecture of a **GPU**. A GPU doesn't run complex control code fast, but it can multiply thousands of matrix elements in a single clock cycle, making it the perfect hardware engine for training neural networks.

---

## 🎯 The Big Picture
*   **Amdahl's Law** guides where engineers should invest design budgets.
*   **Locality of Reference** justifies why caches work so well.
*   **Pipelining & ILP** squeeze maximum performance out of a single core.
*   **Data-Level Parallelism (SIMD/GPUs)** is the powerhouse of modern AI and deep learning.
