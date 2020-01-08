# 自动求导机制
import torch
from torch import nn,optim
import torchvision
from torch.autograd import Variable


# Variable 变量
x = Variable(torch.randn(5, 5))
# print(x)
y = Variable(torch.randn(5, 5))
z = Variable(torch.randn(5, 5), requires_grad = True)
a = x + y
# print(a.requires_grad) # False
b = a + z
# print(b.requires_grad) # True

model = torchvision.models.resnet18(pretrained = True)
# print(models)
for param in model.parameters():
    param.requires_grad = False
model.fc = nn.Linear(512, 100)

# print(models)

# OPTIMIZE:
optimizer = optim.SGD(model.fc.parameters(), lr=1e-2, momentum=0.9)
print(optimizer)
