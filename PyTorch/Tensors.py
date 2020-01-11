# from __future__ import print_function
import torch

# 创建一个 5 * 3 矩阵，但是未初始化
x =  torch.empty(5, 3)
print(x)

# 创建一个随机初始化矩阵
y = torch.rand(5, 3)
print(y)

# 全 0 矩阵
z = torch.zeros(5, 3, dtype=torch.long)
print(z)

# 与 x 同维 0 矩阵
a1 = torch.zeros_like(x)
print(a1)

# 与 x 同维 1 矩阵
a2 = torch.ones_like(x)
print(a2)
