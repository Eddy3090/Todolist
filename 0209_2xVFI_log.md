float 训练

* unet_2times_1

  default train on REDS | epoch 310: 27.749475  (red val)

* unet_2times_2
  
  default train on Collected | epoch 362: 35.711521

finetune base on unet_2times_2

* train_2022-01-28-07-27-30
  change lr from 2e-4 to 1e-4, data Collected | epoch 314: 35.86768
  * train_2022-02-07-07-24-16
    change lr from 2e-4 to 1e-4, data Collected | epoch 359: 35.96388
* train_2022-01-28-08-00-28
  change lr from 2e-4 to 1e-4, data REDS | epoch 302: 27.94352  (red val)
  * train_2022-02-07-07-29-52
    change lr from 2e-4 to 1e-4, data Collected | epoch 339: 36.01379
  * train_2022-02-07-07-33-33
    default, data Collected | epoch 350: 36.01837
    * train_2022-02-08-09-31-38
      default, data REDS | epoch 303: 28.03311 (red val)
      * train_2022-02-10-01-37-38
        default, data Collected | epoch 359: 36.21818
      * train_2022-02-10-01-59-45
        default, data mix | epoch 319: 36.45078
        * train_2022-02-14-01-45-28
          default, data mix | epoch 300: 36.53357
    * train_2022-02-08-09-34-32
      change lr from 2e-4 to 1e-4, data REDS | epoch 208: 28.01666 (red val)
* base on train_2022-02-14-01-45-28(psnr 36.53357), add perceptual_loss, save to unet_2times_floatPer
  * train_2022-02-16-02-07-13
    keep lr as 2e-4, perceptual_loss_weight 1.0, data mix | perceptual_loss_weight 过大，指标恶化
  * train_2022-02-16-02-09-37
    keep lr as 2e-4, perceptual_loss_weight 1.0, data mix | epoch 169: 35.69825
  * train_2022-02-16-02-13-59
    keep lr as 2e-4, perceptual_loss_weight 0.1, enlarge weight_decay, activation_decay, data mix | epoch 169: 35.71509
    * train_2022-02-18-01-57-09
      keep lr as 2e-4, perceptual_loss_weight 0.1, enlarge weight_decay, activation_decay, data mix | epoch 168: 35.72119
    * train_2022-02-18-02-09-34
      change lr 1e-4, perceptual_loss_weight 0.1, enlarge weight_decay, activation_decay, data mix | epoch 161: 35.78236
      * train_2022-02-21-02-22-29
        change lr 1e-4, perceptual_loss_weight 0.1, enlarge weight_decay, activation_decay, data mix | epoch 167: 35.8117
* base on train_2022-02-14-01-45-28(psnr 36.53357)
  * train_2022-02-23-03-04-55
    keep lr 2e-4, filmVGG_loss_weight 0.1, enlarge weight_decay, activation_decay, data mix | epoch 164: 36.15389
  * train_2022-02-23-06-18-32
    keep lr 2e-4, filmVGGMat_loss_weight 1.0, enlarge weight_decay, activation_decay, data mix | epoch 165: 36.2646
  * train_2022-02-23-06-35-31
    keep lr 2e-4, filmVGGMat_loss_weight 0.25, enlarge weight_decay, activation_decay, data mix | epoch 169: 36.41063
    * train_2022-02-25-02-29-07
      keep lr 2e-4, filmVGGMat_loss_weight 0.25, weight_activation_decay, data mix | epoch 168: 36.43065, 27.94587
  * 
* base on train_2022-02-14-01-45-28(psnr 36.53357) -- Film
  * train_2022-02-25-02-19-02
    keep lr 2e-4, filmStyle_loss_weight 20.0, weight_activation_decay, data mix | epoch 165: 35.66989, 27.20049
  * train_2022-02-25-02-24-52
    keep lr 2e-4, filmVGGMat_loss_weight 0.25, filmStyle_loss_weight 20.0, weight_activation_decay, data mix | epoch 169: 35.89808, 27.38759
  * train_2022-02-28-03-00-50
    keep lr 1e-4, filmVGGMat_loss_weight 0.25, filmStyle_loss_weight 20.0, weight_activation_decay, data mix | epoch 157: 36.06508, 27.47446
* base on train_2022-02-14-01-45-28(psnr 36.53357) -- Lap
  * train_2022-02-28-02-48-43
    keep lr 2e-4, laplacian_lossv2_weight 0.5, weight_activation_decay, data mix | epoch 150: 36.45138, 28.0602
  * train_2022-02-28-03-41-20
    keep lr 1e-4, laplacian_lossv2_weight 0.5, weight_activation_decay, data mix | epoch 168: 36.4949, 28.07829
* train_2022-02-18-08-00-44
  init train, keep lr as 2e-4, perceptual_loss_weight 0.1, enlarge weight_decay, activation_decay, data mix | epoch 163: 33.49872
  * train_2022-02-21-02-09-11
    keep lr as 2e-4, perceptual_loss_weight 0.1, enlarge weight_decay, activation_decay, data mix | epoch 170: 34.35577
  * train_2022-02-21-06-57-57
    change lr 1e-4, perceptual_loss_weight 0.01, enlarge weight_decay, activation_decay, data mix | epoch 158: 35.05398
* train_2022-02-22-09-56-56
  init train, keep lr 2e-4, perceptualL1_loss_weight 1.0, enlarge weight_decay, activation_decay, data mix | epoch 169: 34.85925
* train_2022-02-23-02-57-52
  init train, keep lr 2e-4, filmVGG_loss_weight 1.0, enlarge weight_decay, activation_decay, data mix | epoch 161: 32.10108
* train_2022-02-25-02-31-31
  init train, keep lr 2e-4, filmVGGMat_loss_weight 1.0, weight_activation_decay, data mix | epoch 170: 35.53798, 27.52014
  * train_2022-02-28-02-09-46
    keep lr 2e-4, filmVGGMat_loss_weight 1.0, weight_activation_decay, data mix | epoch 163: 35.86701, 27.64779
  * train_2022-02-28-02-13-24
    keep lr 2e-4, filmVGGMat_loss_weight 0.25, filmStyle_loss_weight 20.0, weight_activation_decay, data mix | epoch 167: 35.32617, 27.01139
  * train_2022-03-02-02-10-40
    keep lr 5e-5, filmVGGMat_loss_weight 1.0, weight_activation_decay, data mix | epoch 138: 35.69537, 27.58667
  * 



- [ ] 数据集的切换训练（finetune) 可以略微提升指标



qat 训练

* unet_2times_qatCol （base on unet_2times_2）
  default, data Collected | epoch 90: 35.107027
* unet_2times_qatRED（base on unet_2times_2）
  default, data REDS | epoch 80: 27.719430

unet_2times_qat

* train_aimet_2022-01-28-10-04-09（base on unet_2times_2）
  change lr from 2e-5 to 1e-4, data Collected | epoch 78: 35.13154
* train_aimet_2022-02-07-07-45-20  (base on train_2022-01-28-07-27-30)
  default, data Collected | epoch 86: 35.14742
* train_aimet_2022-02-08-06-11-41  (base on train_2022-01-28-07-27-30)
  change lr from 2e-5 to 1e-4, data Collected | epoch 89: 35.20301
* train_aimet_2022-02-08-11-32-14  (base on train_2022-02-07-07-33-33)
  default, niter 116000, data mix | epoch 61: 35.40362
  * train_aimet_2022-02-10-07-10-19
    default, niter 116000, data mix | epoch 58: 35.4624
* train_aimet_2022-02-09-07-35-47  (base on train_2022-02-07-07-33-33)
  change lr from 2e-5 to 1e-4, niter 116000, data mix | epoch 82: 35.4222
  * train_aimet_2022-02-11-02-57-17
    change lr from 2e-5 to 1e-4, niter 116000, data mix | epoch 96: 35.51155
* train_aimet_2022-02-14-01-52-18 (train_2022-02-10-01-59-45)
  change lr from 2e-5 to 1e-4, niter 116000, data mix | epoch 85: 35.70285
* train_aimet_2022-02-14-01-59-01 (train_2022-02-10-01-59-45)
  default, niter 116000, data mix | epoch 72: 35.67912
* train_aimet_2022-02-18-02-24-12 (train_2022-02-14-01-45-28)
  default, niter 116000, data mix | epoch 56: 35.66871
* train_aimet_2022-02-21-01-54-57 (train_2022-02-14-01-45-28)
  change lr 1e-4, niter 116000, data mix | epoch 95: 35.70088


- [ ] lr=2e-5 偏小
- [ ] float base模型的指标越好，qat得到的指标也会偏好



xm@10.241.19.184:/home/xm/project/temp/vfi_server/res/setting
