# 🔢 Tensor Datatypes

> [!NOTE] Source Context
> In PyTorch, every tensor has an associated data type (`dtype`) that defines the format and precision of numerical values stored in memory. Selecting the correct datatype is crucial for managing memory footprint, maximizing floating-point operations per second (FLOPS), and enabling mixed-precision or quantized inference.

---

## 1. PyTorch Datatype Reference Table

| Data Type | PyTorch Dtype (Alias) | Description |
| :--- | :--- | :--- |
| **32-bit Floating Point** | `torch.float32` or `torch.float` | Standard floating-point type used for most deep learning tasks. Provides a balance between precision and memory usage. |
| **64-bit Floating Point** | `torch.float64` or `torch.double` | Double-precision floating point. Useful for high-precision numerical tasks but uses more memory. |
| **16-bit Floating Point** | `torch.float16` or `torch.half` | Half-precision floating point. Commonly used in mixed-precision training to reduce memory and computational overhead on modern GPUs. |
| **BFloat16** | `torch.bfloat16` | Brain floating-point format with reduced precision compared to Float16. Used in mixed-precision training, especially on TPUs and modern GPUs (e.g., Ampere architecture). |
| **8-bit Floating Point** | `torch.float8` | Ultra-low-precision floating point. Used for experimental applications and extreme memory-constrained environments (less common). |
| **8-bit Integer** | `torch.int8` | 8-bit signed integer. Used for quantized models to save memory and computation in inference. |
| **16-bit Integer** | `torch.int16` or `torch.short` | 16-bit signed integer. Useful for special numerical tasks requiring intermediate precision. |
| **32-bit Integer** | `torch.int32` or `torch.int` | Standard signed integer type. Commonly used for indexing and general-purpose numerical tasks. |
| **64-bit Integer** | `torch.int64` or `torch.long` | Long integer type. Often used for large indexing arrays or for tasks involving large numbers. |
| **8-bit Unsigned Integer** | `torch.uint8` | 8-bit unsigned integer. Commonly used for image data (e.g., pixel values between 0 and 255). |
| **Boolean** | `torch.bool` | Boolean type, stores `True` or `False` values. Often used for masks in logical operations. |
| **Complex 64** | `torch.complex64` or `torch.cfloat` | Complex number type with 32-bit real and 32-bit imaginary parts. Used for scientific and signal processing tasks. |
| **Complex 128** | `torch.complex128` or `torch.cdouble` | Complex number type with 64-bit real and 64-bit imaginary parts. Offers higher precision but uses more memory. |
| **Quantized Integer** | `torch.qint8` | Quantized signed 8-bit integer. Used in quantized models for efficient inference. |
| **Quantized Unsigned Integer** | `torch.quint8` | Quantized unsigned 8-bit integer. Often used for quantized tensors in image-related tasks. |

---

## 2. Managing Datatypes in Code

PyTorch provides multiple ways to inspect, cast, and control the datatype of tensors:

### Ⅰ. Inspecting Datatypes
Every tensor exposes a `.dtype` property:
```python
import torch

x = torch.tensor([1, 2, 3])
print(x.dtype)  # Output: torch.int64 (Default for integer lists)

y = torch.tensor([1.0, 2.0, 3.0])
print(y.dtype)  # Output: torch.float32 (Default for float lists)
```

### Ⅱ. Explicit Casting with `.to()`
The most common and flexible way to change datatypes is the `.to()` method, which can also change the target hardware device (e.g., CPU to GPU):
```python
# Cast float32 tensor to float16
x_half = y.to(torch.float16)

# Cast and move to GPU simultaneously
x_gpu_half = y.to(device="cuda", dtype=torch.float16)
```

### Ⅲ. Alias Method Casting
PyTorch provides shortcut methods for casting to standard types:
```python
x_long = y.long()      # Cast to torch.int64
x_double = y.double()  # Cast to torch.float64
x_bool = y.bool()      # Cast to torch.bool
```

---

**Related Notes**:
* [[Tensors]]
* [[Pytorch]]
