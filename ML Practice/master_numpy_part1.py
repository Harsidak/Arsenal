"""
===============================================================================
MASTER NUMPY — Part 1: Foundations, Indexing, Broadcasting, Reshaping
===============================================================================
What an elite AI engineer must know about NumPy.
Run each section, read the output, modify and experiment.
"""

import numpy as np
np.set_printoptions(precision=4, suppress=True)

# ============================================================================
# 1. ARRAY CREATION & DTYPES
# ============================================================================
# Why this matters: Every tensor in PyTorch, every weight matrix, every gradient
# is fundamentally a multi-dimensional array. You must think in arrays.

print("=" * 60)
print("1. ARRAY CREATION & DTYPES")
print("=" * 60)

# From Python lists
a = np.array([1, 2, 3])
b = np.array([[1, 2], [3, 4], [5, 6]])  # 2D: shape (3, 2)

print(f"1D array: {a}, shape: {a.shape}, ndim: {a.ndim}, dtype: {a.dtype}")
print(f"2D array:\n{b}\nshape: {b.shape}, ndim: {b.ndim}")

# DTYPE MATTERS — in ML, dtype = memory = speed = precision
# float64 (default) → 8 bytes per element — unnecessarily precise for ML
# float32           → 4 bytes — standard training dtype
# float16           → 2 bytes — mixed precision training
# bfloat16 is NOT in numpy — it's in PyTorch/JAX only

x_64 = np.array([1.0, 2.0, 3.0])                    # default float64
x_32 = np.array([1.0, 2.0, 3.0], dtype=np.float32)   # ML standard
x_16 = np.array([1.0, 2.0, 3.0], dtype=np.float16)   # half precision

print(f"\nfloat64: {x_64.nbytes} bytes for {x_64.size} elements")
print(f"float32: {x_32.nbytes} bytes for {x_32.size} elements")
print(f"float16: {x_16.nbytes} bytes for {x_16.size} elements")

# KEY INSIGHT: A 7B parameter model in float32 = 7e9 * 4 bytes = 28 GB
# Same model in float16 = 14 GB. This is why dtype matters.
print(f"\n7B model memory: fp32={7e9*4/1e9:.0f}GB, fp16={7e9*2/1e9:.0f}GB")

# Common creation functions
zeros = np.zeros((3, 4))          # All zeros — bias initialization
ones = np.ones((2, 3))            # All ones
eye = np.eye(4)                   # Identity matrix — crucial in linear algebra
arange = np.arange(0, 10, 2)     # Like Python range but returns array
linspace = np.linspace(0, 1, 5)  # Evenly spaced — useful for learning rate schedules

print(f"\nIdentity matrix (4x4):\n{eye}")
print(f"Linspace [0,1] with 5 points: {linspace}")

# Random arrays — you'll use these constantly for initialization
rng = np.random.default_rng(42)  # ALWAYS seed for reproducibility

# Xavier/Glorot initialization: scale = sqrt(2 / (fan_in + fan_out))
fan_in, fan_out = 768, 3072  # Typical transformer FFN dimensions
xavier_scale = np.sqrt(2.0 / (fan_in + fan_out))
weights = rng.normal(0, xavier_scale, size=(fan_in, fan_out))
print(f"\nXavier init weights: shape={weights.shape}, std={weights.std():.6f}")
print(f"Expected std: {xavier_scale:.6f}")


# ============================================================================
# 2. INDEXING & SLICING — Think Like a Surgeon
# ============================================================================
# Why this matters: Selecting specific tokens, masking padding, extracting
# attention heads — all indexing operations.

print("\n" + "=" * 60)
print("2. INDEXING & SLICING")
print("=" * 60)

# Create a fake batch of embeddings: (batch=2, seq_len=5, d_model=4)
embeddings = rng.normal(size=(2, 5, 4)).astype(np.float32)
print(f"Embeddings shape: {embeddings.shape}")

# Basic slicing — returns VIEWS (no memory copy!)
first_sample = embeddings[0]         # shape: (5, 4) — first item in batch
first_token = embeddings[0, 0]       # shape: (4,) — CLS token embedding
last_two_tokens = embeddings[:, -2:] # shape: (2, 2, 4) — last 2 tokens, all batches

print(f"First sample shape: {first_sample.shape}")
print(f"First token: {first_token}")
print(f"Last 2 tokens shape: {last_two_tokens.shape}")

# BOOLEAN INDEXING — The backbone of masking in ML
# Example: mask out padding tokens
seq_lengths = np.array([3, 5])  # First sequence has 3 real tokens, second has 5
mask = np.arange(5)[None, :] < seq_lengths[:, None]  # Broadcasting!
print(f"\nAttention mask:\n{mask}")
# True = real token, False = padding
# This is EXACTLY how padding masks work in transformers

# Apply mask to zero out padding embeddings
masked_embeddings = embeddings * mask[:, :, None]  # Broadcast mask to embedding dim
print(f"Masked embeddings[0] (only first 3 tokens non-zero):\n{masked_embeddings[0]}")

# FANCY INDEXING — Select specific elements with index arrays
# Example: gather operation (used in token prediction)
vocab_size = 10
logits = rng.normal(size=(3, vocab_size))  # 3 tokens, vocab=10
target_tokens = np.array([2, 7, 4])        # Ground truth token IDs

# Get the logit for each target token — this is what cross-entropy needs
selected_logits = logits[np.arange(3), target_tokens]
print(f"\nLogits shape: {logits.shape}")
print(f"Selected logits for targets {target_tokens}: {selected_logits}")

# np.where — conditional selection (used everywhere)
# Example: replace negative values with 0 (ReLU!)
x = rng.normal(size=(2, 5))
relu_output = np.where(x > 0, x, 0)  # This IS ReLU
print(f"\nInput:\n{x}")
print(f"ReLU output:\n{relu_output}")


# ============================================================================
# 3. BROADCASTING — THE MOST IMPORTANT NUMPY CONCEPT FOR ML
# ============================================================================
# If you don't master broadcasting, you will write slow loops forever.
# Broadcasting = how NumPy handles operations between different-shaped arrays.

print("\n" + "=" * 60)
print("3. BROADCASTING")
print("=" * 60)

# RULE: Dimensions are compared right-to-left.
# Two dimensions are compatible if: (1) they're equal, or (2) one of them is 1.
# A missing dimension is treated as 1.

# Example 1: Subtract mean from each row (centering data)
data = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]], dtype=np.float32)

row_means = data.mean(axis=1, keepdims=True)  # shape: (3, 1)
centered = data - row_means                    # (3, 3) - (3, 1) → broadcasts!
print("Data:\n", data)
print(f"Row means: {row_means.flatten()}")
print("Centered:\n", centered)
print(f"New row means (should be ~0): {centered.mean(axis=1)}")

# Example 2: Pairwise distances — NO LOOPS
# Given N points in D dimensions, compute all N×N distances
N, D = 5, 3
points = rng.normal(size=(N, D))

# The trick: reshape to enable broadcasting
# points[:, None, :] has shape (N, 1, D)
# points[None, :, :] has shape (1, N, D)
# Subtraction broadcasts to (N, N, D)
diff = points[:, None, :] - points[None, :, :]  # (N, N, D)
distances = np.sqrt((diff ** 2).sum(axis=-1))     # (N, N)
print(f"\nPairwise distance matrix ({N}x{N}):\n{distances}")

# Example 3: Softmax — used in EVERY transformer forward pass
def softmax(x, axis=-1):
    """Numerically stable softmax using broadcasting."""
    # Subtract max for numerical stability (log-sum-exp trick)
    x_max = x.max(axis=axis, keepdims=True)   # broadcasts back
    exp_x = np.exp(x - x_max)                  # broadcasts: (N, C) - (N, 1)
    return exp_x / exp_x.sum(axis=axis, keepdims=True)  # broadcasts

logits = rng.normal(size=(4, 10))  # batch=4, classes=10
probs = softmax(logits)
print(f"\nSoftmax output shape: {probs.shape}")
print(f"Row sums (should be 1.0): {probs.sum(axis=1)}")
print(f"All positive: {(probs > 0).all()}")

# Example 4: Outer product via broadcasting — builds attention score matrices
q = rng.normal(size=(8,))  # query vector
k = rng.normal(size=(8,))  # key vector
# Outer product: (8, 1) * (1, 8) → (8, 8)
outer = q[:, None] * k[None, :]
print(f"\nOuter product shape: {outer.shape}")

# CRITICAL BROADCASTING PATTERNS FOR ML:
print("\n--- Broadcasting Patterns You MUST Know ---")
print("(B, S, D) + (D,)       → bias addition to embeddings")
print("(B, S, D) * (B, S, 1)  → masking (zero out padding)")
print("(B, H, S, 1) + (1, 1, 1, S) → causal mask in attention")
print("(N, 1, D) - (1, M, D)  → pairwise differences")


# ============================================================================
# 4. RESHAPING & DIMENSION MANIPULATION
# ============================================================================
# Why this matters: Transformers constantly reshape tensors —
# splitting into heads, merging heads, flattening for linear layers.

print("\n" + "=" * 60)
print("4. RESHAPING & DIMENSION MANIPULATION")
print("=" * 60)

# reshape — most common operation
x = np.arange(24)
print(f"Original: shape {x.shape}")
print(f"Reshaped to (4,6): shape {x.reshape(4, 6).shape}")
print(f"Reshaped to (2,3,4): shape {x.reshape(2, 3, 4).shape}")
print(f"Using -1 (infer): {x.reshape(2, -1).shape}")  # -1 means "figure it out"

# THE MULTI-HEAD ATTENTION RESHAPE
# This is the most important reshape in all of deep learning
batch, seq_len, d_model = 2, 10, 512
num_heads = 8
d_head = d_model // num_heads  # 64

# Simulate: after linear projection, we have (batch, seq_len, d_model)
qkv = rng.normal(size=(batch, seq_len, d_model)).astype(np.float32)

# Split into heads: (batch, seq_len, d_model) → (batch, seq_len, num_heads, d_head)
qkv_heads = qkv.reshape(batch, seq_len, num_heads, d_head)

# Transpose to: (batch, num_heads, seq_len, d_head) — THIS is the attention layout
qkv_heads = qkv_heads.transpose(0, 2, 1, 3)
print(f"\nMulti-head reshape: {qkv.shape} → {qkv_heads.shape}")
print("(batch, seq_len, d_model) → (batch, num_heads, seq_len, d_head)")

# After attention, merge heads back:
# (batch, num_heads, seq_len, d_head) → (batch, seq_len, d_model)
merged = qkv_heads.transpose(0, 2, 1, 3).reshape(batch, seq_len, d_model)
print(f"Merged back: {merged.shape}")

# transpose vs swapaxes
A = np.zeros((2, 3, 4))
print(f"\ntranspose(0,2,1): {A.transpose(0, 2, 1).shape}")  # (2, 4, 3)
print(f"swapaxes(1,2):    {A.swapaxes(1, 2).shape}")        # same thing for 2 axes

# squeeze and expand_dims
x = np.zeros((1, 5, 1, 3))
print(f"\nOriginal: {x.shape}")
print(f"squeeze():    {x.squeeze().shape}")        # removes ALL size-1 dims → (5, 3)
print(f"squeeze(0):   {np.squeeze(x, 0).shape}")   # removes only axis 0 → (5, 1, 3)

y = np.zeros((5, 3))
print(f"expand_dims(0): {np.expand_dims(y, 0).shape}")  # (1, 5, 3) — add batch dim
print(f"y[None, :, :]:  {y[None].shape}")                # same thing, more idiomatic

# np.newaxis — same as None, used to add dimensions for broadcasting
v = np.array([1, 2, 3])  # shape (3,)
print(f"\nv[:, None] shape: {v[:, None].shape}")  # (3, 1) — column vector
print(f"v[None, :] shape: {v[None, :].shape}")    # (1, 3) — row vector

# stack vs concatenate
a = np.zeros((3, 4))
b = np.ones((3, 4))
print(f"\nstack([a,b], axis=0): {np.stack([a, b], axis=0).shape}")    # (2, 3, 4) NEW dim
print(f"concatenate([a,b], axis=0): {np.concatenate([a, b], axis=0).shape}")  # (6, 4) EXISTING dim


# ============================================================================
# 5. VIEWS vs COPIES — Understanding Memory
# ============================================================================
# Why this matters: Views share memory (fast, zero-copy). Copies don't.
# Getting this wrong causes subtle bugs or unexpected memory usage.

print("\n" + "=" * 60)
print("5. VIEWS vs COPIES")
print("=" * 60)

original = np.array([1, 2, 3, 4, 5])

# Slicing creates a VIEW (shared memory)
view = original[1:4]
view[0] = 99
print(f"After modifying view: original = {original}")  # original is modified!

# Copy creates independent memory
original = np.array([1, 2, 3, 4, 5])
copy = original[1:4].copy()
copy[0] = 99
print(f"After modifying copy: original = {original}")  # original unchanged

# How to check: np.shares_memory()
a = np.zeros((3, 4))
b = a[0]           # view
c = a[0].copy()    # copy
print(f"\nb shares memory with a: {np.shares_memory(a, b)}")  # True
print(f"c shares memory with a: {np.shares_memory(a, c)}")    # False

# reshape returns view when possible, copy when not
x = np.arange(12)
y = x.reshape(3, 4)  # view — contiguous memory
print(f"\nreshape is view: {np.shares_memory(x, y)}")

# transpose makes memory non-contiguous
z = y.T
print(f"transpose is view: {np.shares_memory(y, z)}")
print(f"but z is contiguous: {z.flags['C_CONTIGUOUS']}")  # False!
# This is why .contiguous() exists in PyTorch

# STRIDES — how NumPy navigates memory
print(f"\ny strides: {y.strides}")  # (32, 8) for float64: skip 32 bytes for row, 8 for col
print(f"y.T strides: {z.strides}") # (8, 32) — transposed strides


print("\n" + "=" * 60)
print("PART 1 COMPLETE — Run master_numpy_part2.py next")
print("=" * 60)
