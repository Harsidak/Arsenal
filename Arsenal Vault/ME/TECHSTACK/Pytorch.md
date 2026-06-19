# 🔥 PyTorch

> [!NOTE] Source Context
> This note serves as the entry point for learning **PyTorch** in the Arsenal vault. It builds upon mathematical fundamentals of vector/matrix operations and details the library's role as a leading platform for deep learning prototyping and production.

---

## 1. What is PyTorch?

**PyTorch** is a premier open-source machine learning framework developed by Meta's AI Research lab. At its core, it provides two key capabilities:
1. **GPU-Accelerated Tensor Computation**: High-performance multi-dimensional arrays (tensors) with seamless CUDA support, similar to NumPy but optimized for hardware accelerators.
2. **Dynamic Autograd System**: A tape-based automatic differentiation engine that tracks operations at runtime to compute gradients automatically.

Unlike static frameworks, PyTorch utilizes a **dynamic computational graph** (eager execution). The network architecture is defined dynamically during execution, allowing for pythonic debugging, control flow, and flexible model design.

---

## 2. Core Pillars of PyTorch

### Ⅰ. Tensors: The Lifeblood of PyTorch
Tensors are the fundamental data structures, representing multi-dimensional matrices.
- **NumPy Bridge**: Tensors can easily share memory with CPU-based NumPy arrays.
- **Hardware Agnostic**: Move tensors between CPU, GPU (`cuda`), and Apple Silicon (`mps`) with a simple `.to()` call.

### Ⅱ. Autograd: Automatic Differentiation
The `torch.autograd` package records a graph of all operations executed on tensors, allowing backpropagation at the call of a single function:
```python
loss.backward()  # Computes gradients for all leaf parameters automatically
```

---

## 3. Computational Graphs: Dynamic vs. Static

```
    Static Graph (e.g., TF 1.x)             Dynamic Graph (PyTorch)
    Compile First ──► Run Many              Define-by-Run (On-the-Fly)
       ┌──────────────────┐                    ┌──────────────────┐
       │   Define Graph   │                    │  Run Operations  │
       └────────┬─────────┘                    └────────┬─────────┘
                ▼                                       ▼
       ┌──────────────────┐                    ┌──────────────────┐
       │  Compile Graph   │                    │  Builds Graph    │
       └────────┬─────────┘                    │   Dynamically    │
                ▼                               └──────────────────┘
       ┌──────────────────┐
       │ Feed Data & Run  │
       └──────────────────┘
```

- **Static Graphs**: The network structure is defined, compiled, and optimized beforehand. While efficient, it is notoriously hard to debug.
- **Dynamic Graphs**: The graph is built dynamically as each operation is executed. This makes writing control flow (loops, conditionals) intuitive and allows developers to inspect values using standard Python debuggers (like `pdb`).

---

**Related Notes**:
* [[Vector Spaces]]
* [[Linear Mappings]]
* [[Tensors]]
* [[Tensor Datatypes]]
