**Deep Iterative Frame Interpolation for Full-frame Video Stabilization**  DIFRINT

* end-to-end; unsupervised 
* full-frame video stabilization 
* 训练过程：中间帧$$f_i$$随机空间移动生成伪GT--$$f_s$$，$$f_{i-1}$$/$$f_{i+1}$$通过PWC-Net推理warp到$$f_s$$生成$$f_W^-$$/$$f_W^+$$，经过U-Net生成$$f_{int}$$，$$f_i$$ warp to $$f_{int}$$，经过ResNet生成$$\hat{f_i}$$；
* 推理过程：$$f_{i-1}$$/$$f_{i+1}$$通过PWC-Net推理warp到中间状态$$f_W^-$$/$$f_W^+$$，后续与训练一致；
* 可通过自定义迭代次数和skip parameter 来适应不同的需求。
* drawbacks (from other article)
  * 如不稳定视频中包含大的晃动，估计的光流会不够准确导致生成帧的扭曲和鬼影（尤其是在运动物体的边缘）


![image-20211110195340131](1110_fullFrame.assets/image-20211110195340131.png)

![image-20211110201003889](1110_fullFrame.assets/image-20211110201003889.png)

**Channel Attention Is All You Need for Video Frame Interpolation**  CAIN

* end-to-end
* 不需要运动估计（如光流），使用 PixelShuffle 和 channel attention 完成视频插帧

![image-20211111151614093](1110_fullFrame.assets/image-20211111151614093.png)

![image-20211111151636883](1110_fullFrame.assets/image-20211111151636883.png)

![image-20211111151650887](1110_fullFrame.assets/image-20211111151650887.png)



**Deep Motion Blind Video Stabilization**  

* 原始的DeepStab数据集contain a significant non-overlapping field-of-view, and a perspective mismatch，不利于生成模型的训练
* 改进版本的CAIN用于生成视角稳定的视频数据，方法名为Dataset Generation Pipeline (DGP) ，经过DGP处理过的DeepStab数据用于文中生成模型的训练
* code和文中提及的supplementary material应该还没放出，推理速度说是比最快的还能提升3倍，具体数据未提及。

![image-20211111191413897](1110_fullFrame.assets/image-20211111191413897.png)

![image-20211111191446355](1110_fullFrame.assets/image-20211111191446355.png)



**Out-of-boundary View Synthesis Towards Full-Frame Video Stabilization**  

* 