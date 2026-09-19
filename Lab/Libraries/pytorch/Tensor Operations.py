import numpy as np
import torch as t


def section(title):
    print(f"\n--- {title} ---")


# ============================================================
# PyTorch Tensor Operations: practical notes
# ============================================================
# Core idea:
# - Tensor = n-dimensional array, similar to NumPy ndarray.
# - Most deep learning work is: create tensors, move them to device,
#   reshape them, run math, reduce dimensions, and track gradients.


# ============================================================
# 1. Creating tensors
# ============================================================
section("1. Creating tensors")

# Fast allocation, values are uninitialized memory. Do not trust contents.
empty = t.empty(2, 3)

# Common initialized tensors.
zeros = t.zeros(2, 3)
ones = t.ones(2, 3)
full = t.full((2, 3), 7)

# Random values from a uniform distribution in [0, 1).
random = t.rand(2, 3)

# Reproducible random values.
t.manual_seed(100)
reproducible = t.rand(2, 3)

# Build a tensor from Python data.
x = t.tensor([[1, 2, 3], [4, 5, 6]])

print("type:", type(x))
print("shape:", x.shape)
print("dtype:", x.dtype)
print("device:", x.device)


# ============================================================
# 2. Shape helpers: *_like
# ============================================================
section("2. Shape helpers")

# Use an existing tensor's shape without manually retyping dimensions.
same_empty = t.empty_like(x)
same_zeros = t.zeros_like(x)
same_ones = t.ones_like(x)

# rand_like needs a floating dtype. Integer tensors cannot hold [0, 1) floats.
same_random_float = t.rand_like(x, dtype=t.float32)

print("zeros_like:\n", same_zeros)
print("rand_like float:\n", same_random_float)


# ============================================================
# 3. Dtypes and conversions
# ============================================================
section("3. Dtypes")

ints = t.tensor([1, 2, 3])
floats = t.tensor([1, 2, 3], dtype=t.float32)

# Convert dtype. This returns a new tensor unless assigned back.
ints_as_float = ints.to(t.float32)

# Useful defaults:
# - indexes/classes: int64 / long
# - neural network values: float32
# - high precision math: float64 when needed
print("ints dtype:", ints.dtype)
print("floats dtype:", floats.dtype)
print("converted dtype:", ints_as_float.dtype)


# ============================================================
# 4. Device: CPU vs GPU
# ============================================================
section("4. Device")

device = "cuda" if t.cuda.is_available() else "cpu"

# Put tensors on the selected device.
features = t.tensor([[1, 2, 3], [4, 5, 6]], dtype=t.float32, device=device)
weights = t.tensor([[0.1, 0.2], [0.3, 0.4], [0.5, 0.6]], device=device)

# Rule: tensors in the same operation must be on the same device.
print("selected device:", device)
print("features device:", features.device)


# ============================================================
# 5. Scalar and elementwise operations
# ============================================================
section("5. Scalar and elementwise operations")

a = t.tensor([[1.0, -2.0, 3.0], [-4.0, 5.5, 6.2]])

print("a + 2:\n", a + 2)
print("a * 2:\n", a * 2)
print("a / 2:\n", a / 2)
print("a ** 2:\n", a**2)

# Elementwise functions.
print("abs:\n", t.abs(a))
print("neg:\n", t.neg(a))
print("round:\n", t.round(a))
print("ceil:\n", t.ceil(a))
print("floor:\n", t.floor(a))

# Clamp values into a fixed range.
print("clamp -1 to 4:\n", t.clamp(a, min=-1, max=4))


# ============================================================
# 6. Broadcasting
# ============================================================
section("6. Broadcasting")

# PyTorch automatically expands size-1 dimensions where possible.
matrix = t.tensor([[1, 2, 3], [4, 5, 6]])
row_bias = t.tensor([10, 20, 30])
col_bias = t.tensor([[100], [200]])

print("matrix + row_bias:\n", matrix + row_bias)
print("matrix + col_bias:\n", matrix + col_bias)

# Shape rule from the right side:
# dimensions must be equal, or one of them must be 1.


# ============================================================
# 7. Reductions
# ============================================================
section("7. Reductions")

r = t.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])

print("sum all:", t.sum(r))
print("sum dim=0 columns:", t.sum(r, dim=0))
print("sum dim=1 rows:", t.sum(r, dim=1))
print("mean:", t.mean(r))
print("median:", t.median(r))
print("min:", t.min(r))
print("max:", t.max(r))
print("prod:", t.prod(r))
print("std:", t.std(r))
print("var:", t.var(r))
print("argmax flat index:", t.argmax(r))
print("argmin flat index:", t.argmin(r))

# Keep dimensions when the result must still broadcast later.
print("row sums keepdim:\n", t.sum(r, dim=1, keepdim=True))


# ============================================================
# 8. Matrix operations
# ============================================================
section("8. Matrix operations")

m1 = t.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])      # shape: 2 x 3
m2 = t.tensor([[10.0, 20.0], [30.0, 40.0], [50.0, 60.0]])  # shape: 3 x 2
v1 = t.tensor([1.0, 2.0, 3.0])
v2 = t.tensor([10.0, 20.0, 30.0])
square = t.tensor([[2.0, 1.0], [5.0, 3.0]])

print("matmul:\n", t.matmul(m1, m2))
print("@ operator:\n", m1 @ m2)
print("dot 1D:", t.dot(v1, v2))
print("transpose:\n", t.transpose(m1, 0, 1))
print("det:", t.linalg.det(square))
print("inverse:\n", t.linalg.inv(square))


# ============================================================
# 9. Comparisons and masks
# ============================================================
section("9. Comparisons and masks")

p = t.tensor([[1, 5, 3], [7, 2, 9]])
q = t.tensor([[2, 5, 1], [8, 1, 9]])

mask = p > q
print("p > q:\n", mask)
print("values from p where p > q:", p[mask])

# Use where for vectorized conditional selection.
print("max elementwise via where:\n", t.where(p > q, p, q))


# ============================================================
# 10. Common neural-network functions
# ============================================================
section("10. NN-style functions")

logits = t.tensor([[1.0, 2.0, 3.0], [1.0, 3.0, 2.0]])

print("log:", t.log(t.tensor([1.0, 2.0, 4.0])))
print("exp:", t.exp(t.tensor([0.0, 1.0])))
print("sqrt:", t.sqrt(t.tensor([4.0, 9.0])))
print("sigmoid:\n", t.sigmoid(logits))
print("tanh:\n", t.tanh(logits))
print("relu:\n", t.relu(t.tensor([-2.0, 0.0, 3.0])))

# Softmax converts logits to probabilities along a dimension.
# For class scores shaped [batch, classes], use dim=1.
print("softmax over classes:\n", t.softmax(logits, dim=1))


# ============================================================
# 11. In-place operations
# ============================================================
section("11. In-place operations")

base = t.tensor([1.0, 2.0, 3.0])
base.add_(2)
base.mul_(10)

print("after add_ and mul_:", base)

# In-place functions end with _.
# They save memory, but can break autograd if used on values needed for gradients.


# ============================================================
# 12. Copying and memory
# ============================================================
section("12. Copying and memory")

original = t.tensor([[1, 2, 3], [4, 5, 6]])
alias = original
copy = original.clone()

alias[0, 0] = 999
copy[0, 1] = 888

print("original changed by alias:\n", original)
print("copy is independent:\n", copy)
print("same Python object:", id(original) == id(alias))
print("different Python object:", id(original) != id(copy))


# ============================================================
# 13. Reshaping and dimensions
# ============================================================
section("13. Reshaping")

s = t.arange(1, 7)          # [1, 2, 3, 4, 5, 6]
s2 = s.reshape(2, 3)        # 2 rows, 3 columns
flat = s2.flatten()         # back to 1D
transposed = s2.permute(1, 0)

print("arange:", s)
print("reshape 2x3:\n", s2)
print("flatten:", flat)
print("permute 1,0:\n", transposed)

# view requires compatible, contiguous memory. reshape is more flexible.
viewed = s2.view(3, 2)
print("view 3x2:\n", viewed)

# Add/remove size-1 dimensions.
batched = s2.unsqueeze(0)   # shape: [1, 2, 3]
unbatched = batched.squeeze(0)

print("unsqueeze shape:", batched.shape)
print("squeeze shape:", unbatched.shape)


# ============================================================
# 14. NumPy interop
# ============================================================
section("14. NumPy interop")

np_array = np.array([1, 2, 3])
torch_from_np = t.from_numpy(np_array)
back_to_np = torch_from_np.numpy()

print("from numpy:", torch_from_np)
print("back to numpy:", back_to_np)

# CPU tensors and NumPy arrays can share memory.
# Clone when you need an independent copy:
independent = t.from_numpy(np_array).clone()
np_array[0] = 999
print("shared tensor changed:", torch_from_np)
print("cloned tensor unchanged:", independent)


# ============================================================
# 15. Autograd quick pattern
# ============================================================
section("15. Autograd")

w = t.tensor([2.0, 3.0], requires_grad=True)
loss = (w**2).sum()
loss.backward()

print("loss:", loss.item())
print("gradient d(loss)/dw:", w.grad)

# Training loop pattern:
# 1. forward pass: prediction = model(input)
# 2. loss: compare prediction with target
# 3. backward: loss.backward()
# 4. update weights: optimizer.step()
# 5. clear gradients: optimizer.zero_grad()
