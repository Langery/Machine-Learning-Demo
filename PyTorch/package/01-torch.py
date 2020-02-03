import torch, numpy
import numpy as np

# Creation Ops
# Two-dimensional tensor
a = torch.eye(3)
# a = torch.eye(5)
print(a)

b = np.array([1, 2, 3])
t = torch.from_numpy(b)
print(t)

torch.LongTensor([1, 2, 3])
t[0] = -1
print(b)

# linspace 返回一个一维张量
print(torch.linspace(3, 10, steps=5))
print(torch.linspace(-10, 10, steps=5))

print(torch.ones(2, 3))
