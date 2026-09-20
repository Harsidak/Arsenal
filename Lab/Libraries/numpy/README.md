# NumPy

Mathematical computing drills — matrix operations, broadcasting, implementing algorithms from Axler/Joseph computationally.

## Drills

- `matrix_ops.py` — basic operations, slicing, reshaping
- `linalg.py` — eigenvalues, SVD, solving systems
- `broadcasting.py` — understand broadcasting rules by breaking them

## Usage

Quick verification of a math derivation:
```python
python -c "import numpy as np; A = np.array([[1,2],[3,4]]); print(np.linalg.eig(A))"
```

Or use `Lab/scratch/math.py` for throwaway work.
