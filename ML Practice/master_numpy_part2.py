"""
===============================================================================
MASTER NUMPY — Part 2: Linear Algebra & Einsum
===============================================================================
The mathematical backbone of deep learning, implemented in NumPy.
"""

import numpy as np
np.set_printoptions(precision=4, suppress=True)
rng = np.random.default_rng(42)

# ============================================================================
# 6. LINEAR ALGEBRA — The Language of Deep Learning
# ============================================================================

print("=" * 60)
print("6. LINEAR ALGEBRA")
print("=" * 60)

# --- Matrix Multiplication ---
# THE most common operation in deep learning. Every linear layer is matmul.

# Linear layer: y = xW + b
batch, in_features, out_features = 4, 768, 3072
x = rng.normal(size=(batch, in_features)).astype(np.float32)
W = rng.normal(size=(in_features, out_features)).astype(np.float32) * 0.01
b = np.zeros(out_features, dtype=np.float32)

# Three equivalent ways to do matmul:
y1 = np.matmul(x, W) + b   # explicit
y2 = x @ W + b              # operator — USE THIS, it's cleanest
y3 = np.dot(x, W) + b       # works for 2D, but @ is better for batched

print(f"Linear layer: ({batch}, {in_features}) @ ({in_features}, {out_features}) = {y1.shape}")
assert np.allclose(y1, y2) and np.allclose(y2, y3)

# Batched matmul — attention scores = Q @ K^T
B, H, S, D = 2, 8, 10, 64  # batch, heads, seq_len, d_head
Q = rng.normal(size=(B, H, S, D)).astype(np.float32)
K = rng.normal(size=(B, H, S, D)).astype(np.float32)

# @ broadcasts over batch dims: (B,H,S,D) @ (B,H,D,S) → (B,H,S,S)
attention_scores = Q @ K.transpose(0, 1, 3, 2) / np.sqrt(D)
print(f"Attention scores: Q{Q.shape} @ K^T → {attention_scores.shape}")

# --- Norms ---
# Used for: normalization, regularization, gradient clipping

v = np.array([3.0, 4.0])
print(f"\nL2 norm of {v}: {np.linalg.norm(v)}")           # 5.0
print(f"L1 norm of {v}: {np.linalg.norm(v, ord=1)}")      # 7.0
print(f"Inf norm of {v}: {np.linalg.norm(v, ord=np.inf)}") # 4.0

# Frobenius norm for matrices — used in weight decay
W_small = rng.normal(size=(3, 3))
print(f"Frobenius norm: {np.linalg.norm(W_small, 'fro'):.4f}")
print(f"Same as sqrt(sum(W²)): {np.sqrt(np.sum(W_small**2)):.4f}")

# Gradient clipping by norm
def clip_grad_norm(grads, max_norm=1.0):
    """Clip gradients by global norm — exactly what PyTorch does."""
    total_norm = np.sqrt(sum(np.sum(g**2) for g in grads))
    clip_coef = max_norm / (total_norm + 1e-6)
    if clip_coef < 1.0:
        grads = [g * clip_coef for g in grads]
    return grads, total_norm

fake_grads = [rng.normal(size=(10, 10)) * 5 for _ in range(3)]
clipped, norm = clip_grad_norm(fake_grads)
print(f"\nGrad norm before clip: {norm:.4f}")
clipped_norm = np.sqrt(sum(np.sum(g**2) for g in clipped))
print(f"Grad norm after clip:  {clipped_norm:.4f}")

# --- Eigendecomposition ---
# Why: PCA, spectral methods, understanding covariance matrices

# Symmetric matrix (covariance matrices are always symmetric)
A = rng.normal(size=(4, 4))
cov = A.T @ A  # Guaranteed symmetric positive semi-definite

eigenvalues, eigenvectors = np.linalg.eigh(cov)  # eigh for symmetric (faster, stabler)
print(f"\nEigenvalues of covariance matrix: {eigenvalues}")
print(f"All positive (PSD check): {(eigenvalues >= -1e-10).all()}")

# Verify: A @ v = λ * v
v0 = eigenvectors[:, 0]
print(f"A @ v = {cov @ v0}")
print(f"λ * v = {eigenvalues[0] * v0}")

# --- SVD (Singular Value Decomposition) ---
# Why: LoRA is literally SVD. Dimensionality reduction. Data compression.

M = rng.normal(size=(5, 3))
U, S, Vt = np.linalg.svd(M, full_matrices=False)
print(f"\nSVD: M({M.shape}) = U({U.shape}) @ diag(S)({S.shape}) @ Vt({Vt.shape})")

# Verify reconstruction
M_reconstructed = U @ np.diag(S) @ Vt
print(f"Reconstruction error: {np.linalg.norm(M - M_reconstructed):.2e}")

# Low-rank approximation — THIS IS WHAT LoRA DOES
# Keep only top-k singular values
rank = 2
M_lowrank = U[:, :rank] @ np.diag(S[:rank]) @ Vt[:rank, :]
error = np.linalg.norm(M - M_lowrank) / np.linalg.norm(M)
print(f"Rank-{rank} approximation relative error: {error:.4f}")
print(f"Compression: {M.size} params → {U[:,:rank].size + S[:rank].size + Vt[:rank].size} params")

# --- Solve Linear Systems ---
# Why: Normal equations in linear regression, Cholesky-based sampling

A = rng.normal(size=(3, 3))
b = rng.normal(size=(3,))
x = np.linalg.solve(A, b)  # Solves Ax = b. DON'T use inv(A) @ b — it's slower and less stable
print(f"\nSolving Ax = b:")
print(f"Residual ||Ax - b||: {np.linalg.norm(A @ x - b):.2e}")

# --- Determinant and Inverse ---
print(f"\ndet(A) = {np.linalg.det(A):.4f}")
A_inv = np.linalg.inv(A)
print(f"A @ A_inv ≈ I: {np.allclose(A @ A_inv, np.eye(3))}")

# --- Cholesky Decomposition ---
# Why: Efficient sampling from multivariate Gaussians, GP inference
cov = np.array([[2.0, 0.5], [0.5, 1.0]])
L = np.linalg.cholesky(cov)  # Lower triangular: cov = L @ L^T
print(f"\nCholesky of covariance:\n{L}")
print(f"Reconstruction check: {np.allclose(L @ L.T, cov)}")

# Sample from multivariate Gaussian using Cholesky
mean = np.array([1.0, 2.0])
samples = mean + (L @ rng.normal(size=(2, 1000))).T  # (1000, 2)
print(f"Sample mean: {samples.mean(axis=0)} (expected: {mean})")
print(f"Sample cov:\n{np.cov(samples.T)}\n(expected:\n{cov})")


# ============================================================================
# 7. EINSUM — The Universal Tensor Operation
# ============================================================================
# einsum can express ANY tensor contraction. Once you master it,
# you can read and write any tensor operation in a single line.

print("\n" + "=" * 60)
print("7. EINSUM — The Universal Tensor Operation")
print("=" * 60)

# SYNTAX: np.einsum('input_subscripts -> output_subscripts', *tensors)
# - Each letter = one axis
# - Repeated letters = those axes get contracted (summed over)
# - Output subscripts = what dimensions remain

# --- Dot product ---
a = np.array([1, 2, 3], dtype=float)
b = np.array([4, 5, 6], dtype=float)
print(f"Dot product: {np.einsum('i,i->', a, b)}")  # sum over i → scalar
# Same as: np.dot(a, b)

# --- Matrix multiply ---
A = rng.normal(size=(3, 4))
B = rng.normal(size=(4, 5))
C = np.einsum('ik,kj->ij', A, B)  # k is repeated → summed
print(f"Matmul: (3,4) @ (4,5) = {C.shape}")
assert np.allclose(C, A @ B)

# --- Batched matmul ---
# This is how attention works: Q @ K^T for each batch and head
Q = rng.normal(size=(2, 8, 10, 64))  # (batch, heads, seq, d_head)
K = rng.normal(size=(2, 8, 10, 64))
scores = np.einsum('bhsd,bhtd->bhst', Q, K)  # d contracted, s and t remain
print(f"Attention scores via einsum: {scores.shape}")  # (2, 8, 10, 10)

# --- Outer product ---
a = np.array([1, 2, 3])
b = np.array([4, 5])
outer = np.einsum('i,j->ij', a, b)
print(f"\nOuter product:\n{outer}")

# --- Trace ---
M = np.array([[1, 2], [3, 4]])
print(f"Trace: {np.einsum('ii->', M)}")  # diagonal sum

# --- Transpose ---
A = rng.normal(size=(3, 4))
AT = np.einsum('ij->ji', A)
assert np.allclose(AT, A.T)
print(f"Transpose via einsum: {A.shape} → {AT.shape}")

# --- Batch diagonal ---
batch_matrices = rng.normal(size=(5, 3, 3))
diags = np.einsum('bii->bi', batch_matrices)  # extract diagonals
print(f"\nBatch diagonals: {batch_matrices.shape} → {diags.shape}")

# --- Element-wise multiply then sum (common in loss functions) ---
predictions = rng.normal(size=(4, 10))
targets_onehot = np.eye(10)[np.array([2, 5, 1, 8])]  # one-hot
# This is the core of cross-entropy: sum of pred * target per sample
per_sample = np.einsum('bc,bc->b', predictions, targets_onehot)
print(f"Per-sample dot products: {per_sample}")

# --- EINSUM CHEAT SHEET ---
print("\n--- EINSUM CHEAT SHEET ---")
print("'i,i->'       : dot product")
print("'ik,kj->ij'   : matrix multiply")
print("'bhsd,bhtd->bhst' : batched matmul (attention)")
print("'i,j->ij'     : outer product")
print("'ii->'        : trace")
print("'ij->ji'      : transpose")
print("'bii->bi'     : batch diagonal")
print("'bc,bc->b'    : element-wise multiply + sum per batch")
print("'ijk->ij'     : sum over last axis")
print("'...ij,...jk->...ik' : generalized batched matmul")


# ============================================================================
# 8. IMPLEMENTING ML OPERATIONS FROM SCRATCH
# ============================================================================
# This is where you prove you understand, not just use.

print("\n" + "=" * 60)
print("8. ML OPERATIONS FROM SCRATCH")
print("=" * 60)

# --- Layer Normalization ---
def layer_norm(x, gamma, beta, eps=1e-5):
    """LayerNorm as used in Transformers. Normalizes over last dimension."""
    mean = x.mean(axis=-1, keepdims=True)
    var = x.var(axis=-1, keepdims=True)
    x_norm = (x - mean) / np.sqrt(var + eps)
    return gamma * x_norm + beta

x = rng.normal(size=(2, 5, 8)).astype(np.float32)  # (batch, seq, d_model)
gamma = np.ones(8, dtype=np.float32)
beta = np.zeros(8, dtype=np.float32)
normed = layer_norm(x, gamma, beta)
print(f"LayerNorm output mean per token: {normed[0, 0].mean():.6f} (≈0)")
print(f"LayerNorm output var per token:  {normed[0, 0].var():.6f} (≈1)")

# --- Cross-Entropy Loss ---
def cross_entropy_loss(logits, targets):
    """Cross-entropy with log-sum-exp trick for numerical stability."""
    # logits: (N, C), targets: (N,) integer class indices
    # Step 1: log-softmax (numerically stable)
    log_sum_exp = np.log(np.sum(np.exp(logits - logits.max(axis=1, keepdims=True)),
                                 axis=1, keepdims=True)) + logits.max(axis=1, keepdims=True)
    log_probs = logits - log_sum_exp

    # Step 2: select log prob of correct class (negative log likelihood)
    N = logits.shape[0]
    loss = -log_probs[np.arange(N), targets].mean()
    return loss

logits = rng.normal(size=(8, 100))  # 8 samples, 100 classes
targets = rng.integers(0, 100, size=8)
loss = cross_entropy_loss(logits, targets)
print(f"\nCross-entropy loss: {loss:.4f}")
print(f"Expected for random (ln(100)): {np.log(100):.4f}")

# --- Self-Attention (Single Head) ---
def self_attention(x, W_q, W_k, W_v):
    """Single-head self-attention from scratch."""
    Q = x @ W_q  # (S, D) @ (D, d_k) → (S, d_k)
    K = x @ W_k
    V = x @ W_v

    d_k = Q.shape[-1]
    scores = Q @ K.T / np.sqrt(d_k)  # (S, S)

    # Causal mask: prevent attending to future tokens
    S = scores.shape[0]
    causal_mask = np.triu(np.ones((S, S)), k=1) * (-1e9)
    scores = scores + causal_mask

    # Softmax
    scores_max = scores.max(axis=-1, keepdims=True)
    exp_scores = np.exp(scores - scores_max)
    attn_weights = exp_scores / exp_scores.sum(axis=-1, keepdims=True)

    output = attn_weights @ V  # (S, S) @ (S, d_v) → (S, d_v)
    return output, attn_weights

seq_len, d_model, d_k = 6, 16, 8
x = rng.normal(size=(seq_len, d_model)).astype(np.float32)
W_q = rng.normal(size=(d_model, d_k)).astype(np.float32) * 0.1
W_k = rng.normal(size=(d_model, d_k)).astype(np.float32) * 0.1
W_v = rng.normal(size=(d_model, d_k)).astype(np.float32) * 0.1

out, attn = self_attention(x, W_q, W_k, W_v)
print(f"\nSelf-attention output: {out.shape}")
print(f"Attention weights (row sums=1): {attn.sum(axis=-1)}")
print(f"Causal check - first token only attends to itself: {attn[0]}")

# --- Gradient Descent on Linear Regression ---
def linear_regression_gd(X, y, lr=0.01, steps=1000):
    """Gradient descent for linear regression — the simplest optimization loop."""
    n, d = X.shape
    w = np.zeros(d)  # initialize weights
    b = 0.0

    for i in range(steps):
        # Forward
        y_pred = X @ w + b
        loss = np.mean((y_pred - y) ** 2)

        # Backward (analytical gradients)
        dw = (2 / n) * X.T @ (y_pred - y)
        db = (2 / n) * np.sum(y_pred - y)

        # Update
        w -= lr * dw
        b -= lr * db

        if i % 200 == 0:
            print(f"  Step {i:4d}: loss = {loss:.6f}")

    return w, b

print("\nLinear Regression with Gradient Descent:")
X_train = rng.normal(size=(100, 3))
true_w = np.array([2.0, -1.0, 0.5])
y_train = X_train @ true_w + 0.3 + rng.normal(size=100) * 0.1

w_learned, b_learned = linear_regression_gd(X_train, y_train)
print(f"True weights:    {true_w}, bias: 0.3")
print(f"Learned weights: {w_learned}, bias: {b_learned:.4f}")


print("\n" + "=" * 60)
print("PART 2 COMPLETE — Run master_numpy_part3.py next")
print("=" * 60)
