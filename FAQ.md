Frequently used info:

阿里云 https://mirrors.aliyun.com/pypi/simple/

10.53.65.150

```text
pip install torch==1.7.0+cu110 torchvision==0.8.1+cu110 torchaudio===0.7.0 -f https://download.pytorch.org/whl/torch_stable.html

pip3 install torch==1.10.1+cu113 torchvision==0.11.2+cu113 torchaudio==0.10.1+cu113 -f https://download.pytorch.org/whl/cu113/torch_stable.html
```

**conda 环境 site.py 删除新建后，修改内容**

ENABLE_USER_SITE = True
USER_SITE = "/home/xm/program/anaconda3/envs/DUTCode/lib/python3.6"
USER_BASE = "/home/xm/program/anaconda3/envs/DUTCode/lib/python3.6/site-packages"

**变更cuda Toolkit**
cd /usr/local/
sudo rm -rf cuda
sudo ln -s /usr/local/cuda-X.X/ /usr/local/cuda

**ffmpeg使用**

ffmpeg -i DUT_stable.mp4 -s 480*270 -r 15 DUT_stable.gif

ffmpeg -i VID_20211118_124414.mp4 -b:v 15000k -s 960*540 VID_20211118_124414_midRes.mp4

**tar使用**

tar -cvf   sysconfig.tar  /etc/sysconfig
tar -xvf sysconfig.tar
tar -czvf sysconfig.tar.gz /etc/sysconfig/
tar -xzvf sysconfig.tar.gz

**ls -l 衍生**

ls -l |grep -c "^d"   文件夹个数；包括子文件夹 -R

ls -l |grep -c "^-"    文件个数；包括子文件夹 -R

**nvidia-docker安装**

https://www.cnblogs.com/journeyonmyway/p/11234572.html

```
sudo docker run --name ForFlowCal --runtime=nvidia -it -v /home/xm/:/home/xm flownet2:v1 bash
sudo docker run --name FuSta --runtime=nvidia -it -v /home/xm/:/home/xm -v /home/maps/docker_FuSta/zc:/home/zc -p 30001:22 cuda9ssh:v1 bash
```

账户添加

useradd –d /home/zc -m zc

usermod -aG sudo zc

服务器断点续传

rsync -avzP file root@172.20.7.219:/root/tmp

本地工作站重启网络连接  dhclient eno1
