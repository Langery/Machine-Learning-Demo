## Deepsort  techniques

[引：]
&emsp;VOT/SOT：单目标追踪
&emsp;MOT：多目标跟踪
  1. 检测
  2. 特征提取、运动预测
  3. 相似度计算 
  4. 数据关联

### 内容

1. **追踪模块和状态估计**

&emsp;&emsp;卡尔曼滤波估计

2. **分配问题**

&emsp;&emsp;匈牙利算法

$d^{(1)}(i,j)=(d_j-y_i)^TS_i^{-1}(d_j-y_i)$

$d^{(2)}(i,j)=min\{1-r_j^Tr^{(i)}_k|r^{(i)}_k\in R_i\}$

$c_{i,j}=\lambda d^{(1)}(i,j)+(1-\lambda)d^{(2)}(i,j)$

[参考文献]
1. [多目标追踪利器--Deep Sort](https://zhuanlan.zhihu.com/p/45745892)
