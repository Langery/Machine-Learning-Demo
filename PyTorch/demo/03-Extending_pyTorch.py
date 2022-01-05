import torch

# Function
'''
  定义 Function
'''
class Linear(Function):
  def forward(ctx, input, weight, bias=None):
    self.save_for_backward(input, weight, bias)
    output = input.mm(weight.t())
    if bias is not None:
      output += bias.unsqueeze(0).expand_as(output)
    return output
  def backward(ctx, grad_output):
    input, weight, bias = ctx.saved_tensors
    grad_input = grad_weight = grad_bias = None

    if ctx.needs_input_grad[0]:
      grad_input = grad_output.mm(weight)
    if ctx.needs_input_grad[1]:
      grad_weight = grad_output.t().mm(input)
    if bias is not None and ctx.needs_input_grad[2]:
      grad_bias = grad_output.sum(0).squeeze(0)
    
    return grad_input, grad_weight, grad_bias

# used
def linear(input, weight, bias=None):
  return Linear()(input, weight, bias)
