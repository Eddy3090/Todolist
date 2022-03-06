| 2019 | CVPR  | Robust Video  Stabilization by Optimization in CNN Weight Space |                                                       | AI   | CnnOptim    | Jiyang Yu                                                    | cnn提取光流；非实时，30min300帧                              | z    |      |
| ---- | ----- | ------------------------------------------------------------ | ----------------------------------------------------- | ---- | ----------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ---- | ---- |
| 2018 | CGF   | Deep Video  Stabilization Using Adversarial Networks         |                                                       | AI   | adversarial | Sen-Zhe Xu                                                   | 利用spatial transformer  networks预测单应矩阵。实时，预测warper，比传统方法快；可借鉴 | z    |      |
| 2020 | arXiv | Contentaware unsupervised deep  homography estimation        | [code](https://github.com/JirongZhang/DeepHomography) | AI   |             | [Jirong Zhang](https://arxiv.org/search/cs?searchtype=author&query=Zhang,+J) | 无监督估计相邻帧的全局单应性  *相机有较大运动时，全局单应性可能无效 |      |      |

走路的上下运动

1. 复现新的光流预测网络架构RAFT，网络基于两帧图像的feature maps生成multi-scale 4D correlation volumes，并构建GRU循环单元迭代更新flow；保证每次光流都在高分辨率图上更新，克服了级联金字塔方法中低分辨率光流预测错误无法在高分辨率纠正的问题。demo效果如图

1. 2.本周调研了几篇在线视频稳定的方法，核心思路都是输入历史稳定帧和当前帧，用网络预测当前帧的全局单应矩阵或二维仿射变换；其中一篇预测图像对的单应矩阵，通过网络学习预测类似attention map的mask来突出特征强烈的区域，减弱干扰区域（无纹理，光照弱，运动前景）的影响，从而提高全局单应矩阵的预测准确性，这个思路后续可以借鉴。



python run-flownet-docker.py --verbose --gpu 0 /flownet2/flownet2/models/FlowNet2/FlowNet2_weights.caffemodel* /flownet2/flownet2/models/FlowNet2/FlowNet2_deploy.prototxt.template data/0000000-imgL.png data/0000001-imgL.png flow.flo

防抖

* 预处理
  * 相机标定 内参
  * 数据时间对齐（frame gyro ois)
  * 图像去模糊
* 后处理
  * 防撞边
    * 预测到撞边，缩小对应旋转或平移，并在时间上平滑
    * 如信任预测结果，平滑放大再缩小（视觉效果可能会差）



20200121

* 测试服务器环境是否可以跑通代码
* 



nvidia-pyindex          1.0.1
nvidia-tensorboard      1.15.0+nv20.11
nvidia-tensorflow       1.15.4+nv20.11
