## YOLO v3

### 介绍

a. DBL

&emsp;卷积 + BN + Leaky relu

b. resn

c. concat

&emsp;张量拼接

### 内容

1. **backbone**

2. **Output**

&emsp;&emsp;yolo v3 输出了 3 个不同尺度的 feature map（y1，y2，y3），其深度都为 255，边长的规律是 13:26:52

&emsp;&emsp;三次检测：32倍降采样，16倍降采样，8倍降采样

&emsp;&emsp;在网络中使用 **up-sample（上采样）** 的原因:网络越深的特征表达效果越好，比如在进行16倍降采样检测，如果直接使用第四次下采样的特征来检测，这样就使用了浅层特征，这样效果一般并不好。如果想使用32倍降采样后的特征，但深层特征的大小太小，因此yolo_v3使用了步长为2的 **up-sample（上采样）**，把 32 倍降采样得到的 feature map 的大小提升一倍，也就成了 16 倍降采样后的维度。同理 8 倍采样也是对 16 倍降采样的特征进行步长为 2 的上采样，这样就可以使用深层特征进行 detection。

> 设定

&emsp;&emsp;yolo v3 设定的是每个网格单元预测3个 box，所以每个 box 需要有 (x, y, w, h, confidence) 五个基本参数，然后还要有 80 个类别的概率。所以3 *(5 + 80) = 255

3. **some tricks**

    $b_x=\sigma(t_x)+c_x$

    $b_y=\sigma(t_y)+c_y$

    $b_w=p_we^{t_w}$

    $b_w=p_he^{t_h}$

    $P_r(object)*IOU(b.object)=\sigma(t_o)$

4. **loss function**

    $(x,y),(w,h),class,confidence$

[参考文献]

1. [一文看懂YOLO v3](https://blog.csdn.net/litt1e/article/details/88907542)
