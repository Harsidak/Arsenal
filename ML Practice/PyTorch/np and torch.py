import numpy as np
import torch as t

a = t.tensor([[1, 2, 3], [4, 5, 6]])

b = a.numpy()  # convert torch tensor to numpy array

type(b)  # <class 'numpy.ndarray'>

c = np.array([[1, 2, 3], [4, 5, 6]])

d = t.from_numpy(c)  # convert numpy array to torch tensor

type(d)  # <class 'torch.Tensor'>
