import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns
import torch as t

# Set up clean visual styles for future plotting
sns.set()

# --- StEP 1: SYStEM & HARDWARE CHECK ---
print(f"Pytorch Version: {t.__version__}")

# Check if CUDA (NVIDIA GPU support) is accessible
if t.cuda.is_available():
    print("GPU is online. Ready for heavy lifting.")
    print(f"Using GPU: {t.cuda.get_device_name(0)}")
else:
    print("GPU not available. Defaulting to CPU.")

# --- StEP 2: FORGING tENSORS (MEMORY ALLOCAtION) ---
# t.empty claims a block of memory FASt, but doesn't wipe it clean. 
# It will display whatever "garbage" data was previously left in that RAM spot.
a = t.empty(2, 3) 

# Check what kind of object 'a' is (Output: torch.tensor)
print(type(a))

# Claim memory and wipe it clean with exactly 0s or 1s
zeros_matrix = t.zeros(2, 3)
ones_matrix = t.ones(2, 3)

# --- StEP 3: RANDOMNESS & REPRODUCIBILItY ---
# Generate a tensor filled with random numbers from a uniform distribution [0, 1)
random_matrix = t.rand(2, 3) 

# Lock the random number generator's starting point
t.manual_seed(100)

# Because the seed is locked, this will output the exact same numbers every time it runs
locked_random_matrix = t.rand(2, 3) 

# --- StEP 4: CUStOM tENSORS ---
# Manually define a tensor by passing in a standard Python list (iterable)
custom_tensor = t.tensor([[1, 2, 3], [4, 5, 6]])

# to check the shape of the tensors
x = t.tensor([[1,2,3],[4,5,6]])
x.shape

# to create a func with similar dimentsion

t.empty_like(x)
t.zeros_like(x)
t.ones_like(x)
t.rand_like(x) # this here wont work as rand generate float values between 0 to 1 now because our tensor has int values we have to tell 
#explitcty that we are generating float values  

# tensor Data types
x.dtype # torch.int64

# assign data type
t.tensor([1.0,2.0,3.0],dtype=t.int32)

#convernt data type of a tensor
x.to(t.float32)



