from __future__ import print_function
import torch

# 创建一个 5 * 3 矩阵，但是未初始化
x =  torch.empty(5, 3)
print(x)

# 创建一个随机初始化矩阵
y = torch.rand(5, 3)
print(y)

z = torch.zeros(5, 3, dtype=torch.long)
print(z)