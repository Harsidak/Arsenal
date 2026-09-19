import numpy as np
import torch as t


# --- StEP 1: SYStEM & HARDWARE CHECK ---
print(f"Pytorch Version: {t.__version__}")

# Check if CUDA (NVIDIA GPU support) is accessible
if t.cuda.is_available():
    print("GPU is online. Ready for heavy lifting.")
    print(f"Using GPU: {t.cuda.get_device_name(0)}")
else:
    print("GPU not available. Defaulting to CPU.")
