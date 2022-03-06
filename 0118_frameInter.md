[技术解码 | 腾讯云视频插帧技术](https://cloud.tencent.com/developer/article/1813604)

![9lln0aibde](0118_frameInter.assets/9lln0aibde.png)

双帧输入--> PWC-Net预测光流 --> Unet光流refine --> 双帧warping --> CNN拟合插入帧
直觉上是用大量数据迭代训练出来的，突破口是光流预测的精度

**Depth-Aware Video Frame Interpolation**    2019

* Depth-Aware Flow Projection
  同一点有多个光流通过时，与传统方式不同（取平均），重点拟合近距离物体的光流效果更好
  $$\displaystyle F_{t\rightarrow 0}(x)=-t\cdot\frac{\sum_{y\in S(x)}w_0(y)\cdot F_{0\rightarrow 1}(y)}{\sum_{y\in S(x)}w_0(y)}, \quad w_0(y)=\frac{1}{D_0(y)} $$

![image-20220118155948740](0118_frameInter.assets/image-20220118155948740.png)

![image-20220118160107804](0118_frameInter.assets/image-20220118160107804.png)



**AdaCoF: Adaptive Collaboration of Flows for Video Frame Interpolation**     2020

![image-20220120142835897](0118_frameInter.assets/image-20220120142835897.png)

![image-20220120143833550](0118_frameInter.assets/image-20220120143833550.png)

$$\displaystyle \hat{I}(i,j)=\sum_{k=0}^{F-1}\sum_{l=0}^{F-1}W_{i,j}^{(k,l)}(i,j)I(i+dk+\alpha_{i,j}^{(k,l)}, j+dl+\beta_{i,j}^{(k,l)})$$
F=5时，$$W,\alpha,\beta \in R^{W\times H \times 25}$$, d为膨胀尺度



**CDFI: Compression-Driven Network Design for Frame Interpolation**  2021

* 压缩驱动的网络设计，以AdaCof为实例，实现10倍压缩
* 稀疏优化pruning思想
* 以压缩架构为baseline，加入feature pyramid和path selection，提升性能

![image-20220120163342410](0118_frameInter.assets/image-20220120163342410.png)

模型压缩步骤：
1）预训练无压缩模型M0
2）基于权重参数L1稀疏约束的模型重训练
3）根据各层非0权重参数比例降低通道数，形成compact模型M1
4）从头训练M1

![image-20220120163830168](0118_frameInter.assets/image-20220120163830168.png)



**RIFE: Real-Time Intermediate Flow Estimation for Video Frame Interpolation**   2021

* coarse-to-fine IFNet，直接预测中间光流$$F_{t\rightarrow 0}, F_{t\rightarrow 1}$$，不计算$$F_{0\rightarrow 1}, F_{1\rightarrow 0}$$
* teacher-student distillation scheme，student model and the teacher model are jointly trained from scratch   

![image-20220121112122839](0118_frameInter.assets/image-20220121112122839.png)

![image-20220121112207538](0118_frameInter.assets/image-20220121112207538.png)

teacher model额外多出IFBlock^Tea^
多分辨率由粗到细结构
![图片1](0118_frameInter.assets/图片1.png)

交替训练过程中，teacher model的loss没有最后一项
teacher model的输入包含GT，可以训练出更精确的光流，用于指导student model



**FLAVR: Flow-Agnostic Video Representations for Fast Frame Interpolation**  	2021

* 3D时空卷积网络，不预测光流
* channel gating module有助于提高对运动区域的注意力
* 插帧任务的模型encode可用于下游任务（action recognition, optical flow estimation, motion magnification）

![image-20220121150053348](0118_frameInter.assets/image-20220121150053348.png)

**Super SloMo: High Quality Estimation of Multiple Intermediate Frames for Video Interpolation**   2018

* 任意倍数，时间点插帧
* CNN网络预测双向光流$$F_{1\rightarrow 0}, F_{0\rightarrow 1}$$，t时刻光流通过基于时间距离的双线性插值得到$$\hat{F}_{t\rightarrow 0}, \hat{F}_{t\rightarrow 1}$$​，g为基于当前t时刻光流对输入双帧warp的结果，蓝色CNN网络用于refine光流，并预测visibility maps（缓解遮挡效应） 

![image-20220210103509047](0118_frameInter.assets/image-20220210103509047.png)

**Video Frame Interpolation Via Residue Refinement**  RRIN  2020

* residue learning  for refinement

![image-20220210152149990](0118_frameInter.assets/image-20220210152149990.png)

![image-20220210153448207](0118_frameInter.assets/image-20220210153448207.png)

**BMBC:Bilateral Motion Estimation with Bilateral Cost Volume for Video Interpolation**  2020

* 

![image-20220214165439640](0118_frameInter.assets/image-20220214165439640.png)

overview，双边运动估计网络通过不同方式得到t时刻的双向光流，输入帧和上下文map通过光流warp，最后通过动态局部混合滤波器合成得到输出帧

![image-20220214171834831](0118_frameInter.assets/image-20220214171834831.png)

![image-20220214172323925](0118_frameInter.assets/image-20220214172323925.png)

