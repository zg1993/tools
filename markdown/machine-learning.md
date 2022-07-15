#### 部署

#### 机器学习-识别光盘图片

- [github-yolov5](https://github.com/ultralytics/yolov5)
- [yolov5教程入门教程](https://zhuanlan.zhihu.com/p/501798155)

###### 1、环境
  - Python>=3.7.0、PyTorch>=1.7
  - PyTorch pip安装
  ```
  pip3 install torch torchvision torchaudio
  - 依赖安装
  ```
  git clone https://github.com/ultralytics/yolov5  # clone
  cd yolov5
  pip install -r requirements.txt  # install
  ```
  - 安装labelimg(数据标注工具，使用参考入门教程)
  ```
  pip install labelImg
  命令行直接运行
  labelImg
  ```

- [yolov5s.pt 文件模型下载](https://github.com/ultralytics/yolov5/releases)
  - 下载好后将yolov5s.pt文件放在项目的根目录下

- 检测环境是否安装成功
```
python detect.py --source ./data/images/bus.jpg
output
  Speed: 1.7ms pre-process, 104.4ms inference, 6.8ms NMS per image at shape (1, 3, 640, 640)
```
##### 2、训练自己的数据集
 待续
 ./data/plate.yaml
 ```````
  train: images/train
  val: images/val

  nc: 1
  names: ['plate']
 ```
 命令：python train.py --weights yolov5s.pt --data data/plate.yaml --workers 1 --batch-size 8
