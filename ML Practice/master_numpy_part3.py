"""
===============================================================================
MASTER NUMPY — Part 3: Advanced — Numerical Stability, Vectorization,
                        Random Distributions, Performance, and Exercises
===============================================================================
The advanced skills that separate an elite engineer from everyone else.
"""

import numpy as np
import time
np.set_printoptions(precision=4, suppress=True)
rng = np.random.default_rng(42)

# ============================================================================
# 9. NUMERICAL STABILITY — Where Naive Code Silently Breaks
# ============================================================================
# This is THE skill that separates people who "know" NumPy from people
# who can write production ML code.

print("=" * 60)
print("9. NUMERICAL STABILITY")
print("=" * 60)

# --- The Log-Sum-Exp Trick ---
# Problem: computing log(sum(exp(x))) causes overflow/underflow

# WRONG WAY — will overflow for large values
x_large = np.array([1000.0, 1001.0, 1002.0])
try:
    naive = np.log(np.sum(np.exp(x_large)))
    print(f"Naive log-sum-exp: {naive}")  # inf!
except:
    print("Naive log-sum-exp: OVERFLOW")

# RIGHT WAY — subtract max first
def log_sum_exp(x):
    """Numerically stable log-sum-exp."""
    c = x.max()
    return c + np.log(np.sum(np.exp(x - c)))

result = log_sum_exp(x_large)
print(f"Stable log-sum-exp: {result:.4f}")

# This is used EVERYWHERE: softmax, cross-entropy, log-likelihood, VAE ELBO

# --- Softmax Stability ---
def softmax_naive(x):
    """DON'T use this — overflows for large logits."""
    return np.exp(x) / np.sum(np.exp(x), axis=-1, keepdims=True)

def softmax_stable(x):
    """Production-quality softmax."""
    x_shifted = x - x.max(axis=-1, keepdims=True)
    exp_x = np.exp(x_shifted)
    return exp_x / exp_x.sum(axis=-1, keepdims=True)

logits = np.array([[1000, 1001, 1002], [-1000, -999, -998]], dtype=np.float64)
print(f"\nNaive softmax:  {softmax_naive(logits)}")   # NaN or wrong!
print(f"Stable softmax: {softmax_stable(logits)}")    # Correct

# --- Log-Softmax (more stable than log(softmax)) ---
def log_softmax(x):
    """Used in NLLLoss / cross-entropy. More stable than np.log(softmax(x))."""
    x_max = x.max(axis=-1, keepdims=True)
    return x - x_max - np.log(np.sum(np.exp(x - x_max), axis=-1, keepdims=True))

ls = log_softmax(logits)
print(f"Log-softmax:    {ls}")
print(f"Verify: exp(log_softmax) = softmax: {np.allclose(np.exp(ls), softmax_stable(logits))}")

# --- Variance computation: two-pass vs naive ---
# Naive: Var(x) = E[x²] - E[x]² — suffers from catastrophic cancellation
x = np.array([1e8 + 1, 1e8 + 2, 1e8 + 3], dtype=np.float32)
naive_var = np.mean(x**2) - np.mean(x)**2
correct_var = np.var(x)
print(f"\nNaive variance:   {naive_var}")  # Can be negative due to cancellation!
print(f"Correct variance: {correct_var}")

# --- Small epsilon values ---
# Always add eps to denominators to avoid division by zero
x = np.array([0.0, 1.0, 2.0])
# BAD:  1.0 / x  → inf!
# GOOD: 1.0 / (x + 1e-8)
safe_reciprocal = 1.0 / (x + 1e-8)
print(f"\nSafe reciprocal of {x}: {safe_reciprocal}")


# ============================================================================
# 10. VECTORIZATION — Eliminate Every Loop
# ============================================================================
# The #1 performance rule in NumPy: if you wrote a for loop, you did it wrong.

print("\n" + "=" * 60)
print("10. VECTORIZATION & PERFORMANCE")
print("=" * 60)

# --- Example: Computing pairwise cosine similarity ---
N, D = 1000, 128

# SLOW: nested loops
def cosine_sim_loops(X):
    N = X.shape[0]
    sim = np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            sim[i, j] = np.dot(X[i], X[j]) / (np.linalg.norm(X[i]) * np.linalg.norm(X[j]) + 1e-8)
    return sim

# FAST: fully vectorized
def cosine_sim_vectorized(X):
    norms = np.linalg.norm(X, axis=1, keepdims=True)  # (N, 1)
    X_normalized = X / (norms + 1e-8)
    return X_normalized @ X_normalized.T               # (N, N)

X = rng.normal(size=(N, D)).astype(np.float32)

start = time.time()
sim_fast = cosine_sim_vectorized(X)
time_fast = time.time() - start

# Don't run the slow version with N=1000, just demonstrate with small N
X_small = X[:50]
start = time.time()
sim_slow = cosine_sim_loops(X_small)
time_slow = time.time() - start

sim_fast_small = cosine_sim_vectorized(X_small)
print(f"Loop version (N=50):       {time_slow:.4f}s")
print(f"Vectorized (N=50):         {time.time()-time.time():.6f}s")
print(f"Vectorized (N={N}):        {time_fast:.4f}s")
print(f"Results match: {np.allclose(sim_slow, sim_fast_small, atol=1e-5)}")

# --- np.where for conditional operations ---
# Example: Leaky ReLU
def leaky_relu(x, alpha=0.01):
    return np.where(x > 0, x, alpha * x)

x = rng.normal(size=(3, 4))
print(f"\nLeaky ReLU:\n{leaky_relu(x)}")

# --- np.clip — gradient clipping, value bounding ---
gradients = rng.normal(size=(5,)) * 10
clipped = np.clip(gradients, -1.0, 1.0)
print(f"\nGradients:         {gradients}")
print(f"Clipped [-1, 1]:   {clipped}")

# --- Vectorized argmax/argmin ---
logits = rng.normal(size=(4, 10))  # 4 samples, 10 classes
predictions = np.argmax(logits, axis=1)
print(f"\nPredictions (argmax): {predictions}")

# --- Cumulative operations (useful for position IDs, masking) ---
mask = np.array([1, 1, 1, 0, 0, 1, 1, 0])
position_ids = np.cumsum(mask) - 1  # Position IDs respecting mask
print(f"\nMask:         {mask}")
print(f"Position IDs: {position_ids}")


# ============================================================================
# 11. RANDOM DISTRIBUTIONS — Sampling for ML
# ============================================================================
# You need to know these distributions and WHEN to use each.

print("\n" + "=" * 60)
print("11. RANDOM DISTRIBUTIONS FOR ML")
print("=" * 60)

# Use the new Generator API (not the legacy np.random.*)
rng = np.random.default_rng(42)

# --- Uniform [0, 1) — dropout mask ---
dropout_rate = 0.1
x = rng.normal(size=(3, 8))
mask = rng.uniform(size=x.shape) > dropout_rate  # True = keep
scale = 1.0 / (1.0 - dropout_rate)  # Scale up to maintain expected value
x_dropped = x * mask * scale
print(f"Dropout mask (p={dropout_rate}):\n{mask.astype(int)}")
print(f"Fraction kept: {mask.mean():.2f} (expected: {1-dropout_rate})")

# --- Normal/Gaussian — weight initialization ---
# Kaiming (He) init for ReLU networks: std = sqrt(2/fan_in)
fan_in = 512
kaiming_weights = rng.normal(0, np.sqrt(2.0 / fan_in), size=(fan_in, 256))
print(f"\nKaiming init std: expected={np.sqrt(2.0/fan_in):.4f}, actual={kaiming_weights.std():.4f}")

# --- Categorical / Multinomial — token sampling ---
probs = np.array([0.1, 0.3, 0.4, 0.15, 0.05])  # vocabulary probabilities
tokens = rng.choice(len(probs), size=10, p=probs)
print(f"\nSampled tokens: {tokens}")

# Temperature sampling — higher temp = more random
def sample_with_temperature(logits, temperature=1.0):
    """Sample from logits with temperature scaling."""
    scaled = logits / temperature
    # Stable softmax
    probs = np.exp(scaled - scaled.max()) / np.exp(scaled - scaled.max()).sum()
    return rng.choice(len(probs), p=probs)

logits = np.array([2.0, 1.0, 0.5, 0.1, -1.0])
print("\nTemperature sampling (1000 samples each):")
for temp in [0.1, 0.5, 1.0, 2.0]:
    samples = [sample_with_temperature(logits, temp) for _ in range(1000)]
    counts = np.bincount(samples, minlength=5)
    print(f"  T={temp}: {counts} (lower T → more peaked)")

# --- Top-k sampling ---
def top_k_sampling(logits, k=3):
    """Zero out all but top-k logits, then sample."""
    top_k_indices = np.argsort(logits)[-k:]
    filtered = np.full_like(logits, -np.inf)
    filtered[top_k_indices] = logits[top_k_indices]
    probs = np.exp(filtered - filtered.max())
    probs = probs / probs.sum()
    return rng.choice(len(probs), p=probs)

print(f"\nTop-3 sampling from {logits}:")
samples = [top_k_sampling(logits, k=3) for _ in range(1000)]
print(f"  Counts: {np.bincount(samples, minlength=5)} (only top-3 get sampled)")


# ============================================================================
# 12. REDUCTION OPERATIONS — Axis Mastery
# ============================================================================
# Understanding axis= is critical. Get it wrong → silent bugs.

print("\n" + "=" * 60)
print("12. AXIS-AWARE REDUCTIONS")
print("=" * 60)

# Shape: (batch=2, seq_len=3, d_model=4)
x = rng.normal(size=(2, 3, 4))

print(f"Shape: {x.shape}")
print(f"sum():           shape {np.sum(x).shape}")        # scalar — sum everything
print(f"sum(axis=0):     shape {np.sum(x, axis=0).shape}") # (3,4) — sum over batch
print(f"sum(axis=1):     shape {np.sum(x, axis=1).shape}") # (2,4) — sum over seq_len
print(f"sum(axis=2):     shape {np.sum(x, axis=2).shape}") # (2,3) — sum over d_model
print(f"sum(axis=(0,1)): shape {np.sum(x, axis=(0,1)).shape}")  # (4,) — sum batch+seq

# keepdims — ESSENTIAL for broadcasting back
mean = x.mean(axis=-1, keepdims=True)  # (2, 3, 1) — can broadcast with (2, 3, 4)
print(f"\nmean with keepdims: {mean.shape}")
print(f"mean without keepdims: {x.mean(axis=-1).shape}")  # (2, 3) — can't broadcast!

# Rule of thumb: if you're going to use the result for broadcasting, USE keepdims=True


# ============================================================================
# 13. EXERCISES — Prove You Understand
# ============================================================================
# These are NOT optional. Do them without looking at solutions.

print("\n" + "=" * 60)
print("13. EXERCISES")
print("=" * 60)

print("""
EXERCISE 1: Implement batch matrix multiply WITHOUT using @ or np.matmul.
            Use only np.einsum.
            Input: A (B, M, K), B (B, K, N) → Output: (B, M, N)

EXERCISE 2: Implement RMSNorm (used in LLaMA instead of LayerNorm).
            RMSNorm(x) = x / sqrt(mean(x²) + eps) * gamma
            No mean subtraction — simpler and faster than LayerNorm.

EXERCISE 3: Implement cosine similarity attention (not dot-product).
            Attention(Q,K,V) = softmax(cos_sim(Q,K) / tau) @ V
            where cos_sim normalizes Q and K before the dot product.

EXERCISE 4: Given token probabilities (B, S, V), implement nucleus (top-p)
            sampling: sort probs descending, cumsum, mask where cumsum > p.

EXERCISE 5: Implement the GELU activation function:
            GELU(x) = x * Φ(x) where Φ is the Gaussian CDF.
            Use the approximation: 0.5*x*(1 + tanh(sqrt(2/pi)*(x + 0.044715*x³)))

EXERCISE 6: Implement positional encoding (sinusoidal) for a transformer.
            PE(pos, 2i)   = sin(pos / 10000^(2i/d_model))
            PE(pos, 2i+1) = cos(pos / 10000^(2i/d_model))
            Return shape: (max_len, d_model)

EXERCISE 7: Implement batch normalization (training mode).
            BN(x) = gamma * (x - batch_mean) / sqrt(batch_var + eps) + beta
            Input: (B, features). Normalize over the batch dimension.

EXERCISE 8: Implement the KL divergence between two categorical distributions.
            KL(P || Q) = sum(P * log(P/Q))
            Handle zeros properly (0 * log(0) = 0).
""")

# --- SOLUTIONS (scroll down only after attempting!) ---
# .
# .
# .
# .
# .
# .
# .
# .
# .
# .

print("--- SOLUTIONS ---\n")

# Solution 1: Batch matmul with einsum
A = rng.normal(size=(4, 3, 5))
B = rng.normal(size=(4, 5, 2))
C = np.einsum('bmk,bkn->bmn', A, B)
assert np.allclose(C, A @ B)
print(f"Ex 1 ✓ Batch matmul: {A.shape} @ {B.shape} = {C.shape}")

# Solution 2: RMSNorm
def rms_norm(x, gamma, eps=1e-6):
    rms = np.sqrt(np.mean(x ** 2, axis=-1, keepdims=True) + eps)
    return (x / rms) * gamma

x = rng.normal(size=(2, 4, 8))
gamma = np.ones(8)
normed = rms_norm(x, gamma)
print(f"Ex 2 ✓ RMSNorm: rms of output = {np.sqrt(np.mean(normed[0,0]**2)):.4f}")

# Solution 3: Cosine similarity attention
def cosine_attention(Q, K, V, tau=1.0):
    Q_norm = Q / (np.linalg.norm(Q, axis=-1, keepdims=True) + 1e-8)
    K_norm = K / (np.linalg.norm(K, axis=-1, keepdims=True) + 1e-8)
    scores = (Q_norm @ K_norm.T) / tau
    scores = scores - scores.max(axis=-1, keepdims=True)
    attn = np.exp(scores) / np.exp(scores).sum(axis=-1, keepdims=True)
    return attn @ V

Q = rng.normal(size=(5, 16))
K = rng.normal(size=(5, 16))
V = rng.normal(size=(5, 16))
out = cosine_attention(Q, K, V)
print(f"Ex 3 ✓ Cosine attention output: {out.shape}")

# Solution 5: GELU
def gelu(x):
    return 0.5 * x * (1 + np.tanh(np.sqrt(2/np.pi) * (x + 0.044715 * x**3)))

x = np.linspace(-3, 3, 7)
print(f"Ex 5 ✓ GELU({x}) = {gelu(x)}")

# Solution 6: Sinusoidal positional encoding
def positional_encoding(max_len, d_model):
    pos = np.arange(max_len)[:, None]           # (max_len, 1)
    dim = np.arange(0, d_model, 2)[None, :]     # (1, d_model/2)
    angle = pos / (10000 ** (dim / d_model))     # broadcasting!
    pe = np.zeros((max_len, d_model))
    pe[:, 0::2] = np.sin(angle)
    pe[:, 1::2] = np.cos(angle)
    return pe

pe = positional_encoding(100, 64)
print(f"Ex 6 ✓ Positional encoding: {pe.shape}, range: [{pe.min():.1f}, {pe.max():.1f}]")

# Solution 8: KL Divergence
def kl_divergence(P, Q, eps=1e-10):
    """KL(P || Q) with safe handling of zeros."""
    P_safe = np.clip(P, eps, 1.0)
    Q_safe = np.clip(Q, eps, 1.0)
    return np.sum(P_safe * np.log(P_safe / Q_safe))

P = np.array([0.3, 0.5, 0.2])
Q = np.array([0.25, 0.25, 0.5])
print(f"Ex 8 ✓ KL(P||Q) = {kl_divergence(P, Q):.4f}")
print(f"       KL(Q||P) = {kl_divergence(Q, P):.4f} (asymmetric!)")


print("\n" + "=" * 60)
print("ALL PARTS COMPLETE")
print("=" * 60)
print("""
MASTERY CHECKLIST:
  □ Can you write broadcasting operations without trial-and-error?
  □ Can you read any einsum expression and know what it does?
  □ Can you implement softmax, cross-entropy, attention from memory?
  □ Do you know WHY log-sum-exp trick is needed?
  □ Can you diagnose a numerical stability bug in ML code?
  □ Can you look at a loop and immediately vectorize it?
  □ Do you understand views vs copies and memory layout?

If you checked all boxes — you've mastered NumPy for AI engineering.
""")
