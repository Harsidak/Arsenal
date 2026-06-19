# 📦 Tensors

> [!NOTE] Source Context
> Tensors are the fundamental mathematical and computational data structures underpinning modern Deep Learning and AI systems. Originally stemming from linear algebra and physics, in machine learning **Tensors** are generalized multi-dimensional arrays optimized for fast hardware acceleration (GPUs/TPUs) and automatic differentiation.

---

## 1. The Tensor Hierarchy (Dimensionality & Shapes)

A tensor's dimension is called its **Rank** (or Order/Axes). Think of tensors as a nested nesting of arrays:

```
      0D Scalar         1D Vector           2D Matrix             3D Tensor (RGB Image)
        [ 5 ]          [ 1, 2, 3 ]       ┌───┬───┬───┐          ┌───┬───┬───┐ / Red
                                         │ 1 │ 2 │ 3 │          │ 1 │ 2 │ 3 │  / Green
                                         ├───┼───┼───┤          ├───┼───┼───┤   / Blue
                                         │ 4 │ 5 │ 6 │          │ 4 │ 5 │ 6 │  /
                                         └───┴───┴───┘          └───┴───┴───┘ /
```

| Rank | Mathematical Entity | Shape | Example / Real-World Analogy |
| :--- | :--- | :--- | :--- |
| **0D** | **Scalar** | `[]` | A single value (e.g., loss value, temperature, age: `24.0`) |
| **1D** | **Vector** | `[n]` | A list of values (e.g., word embeddings, patient metrics, coordinates) |
| **2D** | **Matrix** | `[m, n]` | A grid of values (e.g., grayscale image, token lookup table, database table) |
| **3D** | **Tensor** | `[c, h, w]` | A stack of matrices (e.g., color RGB image with 3 channels, time-series data) |
| **4D** | **Tensor** | `[b, c, h, w]` | A batch of 3D tensors (e.g., a batch of 32 RGB images fed into a CNN) |
| **5D** | **Tensor** | `[b, t, c, h, w]` | Video data or multi-spectral spatial scans (e.g., batch size $\times$ time frames $\times$ channels $\times$ height $\times$ width) |

---

## 2. Why Are Tensors Used in Deep Learning?

Standard Python lists are highly flexible but slow because they store pointer references to scattered memory locations. Tensors solve this with three structural features:

### Ⅰ. Efficient Contiguous Memory & SIMD
Tensors store numerical data in a **contiguous block of memory** using uniform datatypes (e.g., `float32`). This layout enables CPU/GPU hardware to apply **SIMD (Single Instruction, Multiple Data)** operations, running calculations on hundreds of values in a single clock cycle.

### Ⅱ. Parallel Computation on Accelerators
Modern deep learning models have billions of parameters. Tensors are mathematically structured to be pushed directly onto **GPUs** and **TPUs**, which contain thousands of specialized arithmetic cores designed specifically to perform matrix multiplication in parallel.

### Ⅲ. Dynamic Computational Graph Integration
In frameworks like PyTorch, tensors are not just static data arrays. They contain metadata that tracks their mathematical history (the gradient graph). When a tensor operation occurs, a node is added to the graph, enabling **automatic differentiation (Autograd)** to calculate backward derivatives automatically.

---

## 3. Where Are Tensors Applied in Deep Learning?

```
      [Raw Inputs]  ──►  [Weights / Biases]  ──►  [Forward Ops]  ──►  [Loss & Grads]
      (Data Tensors)     (Parameter Tensors)      (Activation Tensors) (Autograd Tensors)
```

1.  **Data Storage & Pipelines**:
    All real-world data (text, images, audio, video) is converted into tensors before being passed to models. For instance, text is transformed into token index vectors, which are then mapped to embedding tensors.
2.  **Model Parameters (Weights and Biases)**:
    A neural network learns by adjusting its connections. These connections are represented as weight tensors. In a linear layer:
    $$\vec{y} = W\vec{x} + \vec{b}$$
    Where $W$ is a 2D weight matrix tensor, $\vec{x}$ is the input vector tensor, and $\vec{b}$ is the 1D bias vector tensor.
3.  **Forward Activation Flow**:
    As data passes through layers, intermediate mathematical outputs (activations) are carried through the network as dynamic tensors.
4.  **Training & Optimization**:
    During the training loop, loss values are computed as scalar tensors, gradients are calculated as parameter-shaped gradient tensors, and optimization algorithms (like Adam or SGD) update the weights directly using tensor arithmetic.

---

**Related Notes**:
* [[Vector Spaces]]
* [[Linear Mappings]]
* [[Pytorch]]
* [[Tensor Datatypes]] 