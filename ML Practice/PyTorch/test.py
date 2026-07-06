import sympy as sp

# 1. Let's define our subspace W. 
# Imagine W is a 2D plane in 3D space, spanned by these two vectors:
w1 = sp.Matrix([1, 2, 3])
w2 = sp.Matrix([4, 5, 6])

# 2. To find the orthogonal complement (W-perp), we stack w1 and w2 as ROWS in a matrix A.
# This means W is the "Row Space" of A.
A = sp.Matrix([w1.T, w2.T])

print("Matrix A (Rows are basis vectors of W):")
sp.pprint(A)

# 3. W-perp is exactly the Null Space of A (solving A*v = 0).
# SymPy's nullspace() method returns a list of basis vectors for W-perp.
W_perp_basis = A.nullspace()

print("\nBasis for the Orthogonal Complement (W-perp):")
sp.pprint(W_perp_basis)

# 4. Let's prove it! If we dot product our new W-perp vector with w1 or w2, it must be 0.
v_perp = W_perp_basis[0]

dot_1 = w1.dot(v_perp)
dot_2 = w2.dot(v_perp)

print(f"\nDot product of W-perp with w1: {dot_1} (Should be 0)")
print(f"Dot product of W-perp with w2: {dot_2} (Should be 0)")