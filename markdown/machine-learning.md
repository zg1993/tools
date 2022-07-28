#### 部署

#### 机器学习-识别光盘图片

-   [github-yolov5](https://github.com/ultralytics/yolov5)
-   [yolov5教程入门教程](https://zhuanlan.zhihu.com/p/501798155)

###### 1、环境

-   Python>=3.7.0、PyTorch>=1.7
-   PyTorch pip安装
        pip3 install torch torchvision torchaudio
-   依赖安装
        git clone https://github.com/ultralytics/yolov5  # clone
        cd yolov5
        pip install -r requirements.txt  # install
-   安装labelimg(数据标注工具，使用参考入门教程)

        pip install labelImg
        命令行直接运行
        labelImg

-   [yolov5s.pt 文件模型下载](https://github.com/ultralytics/yolov5/releases)

    -   下载好后将yolov5s.pt文件放在项目的根目录下

-   检测环境是否安装成功


    python detect.py --source ./data/images/bus.jpg
    output
      Speed: 1.7ms pre-process, 104.4ms inference, 6.8ms NMS per image at shape (1, 3, 640, 640)


###### 2、训练自己的数据集


 待续
 ./data/plate.yaml(验证集占训练集的0.046)

     train: images/train
     val: images/val

     nc: 1
     names: ['plate']
    ```
    命令：python train.py --weights yolov5s.pt --data data/plate.yaml --workers 1 --batch-size 8 --cache disk

 - --cache 利用磁盘资源加快训练速度
 - --data
 - --weights 允许训练模型权重
 - --cfg 模型结构配置文件
 - --workers
 - --batch-size
 - --resume 继续上次中断的训练

##### 3、数据集制作

###### 选择标准

 - 每类图片大于1500张
 - 每类标注的对象(框框)大于10000
 - 0% ~ 10% 的背景图片(没有标签没有检测对象的图片) 暂定图片总数的1%, 减少过拟合 (防止将背景的特征误认为是物体的特征)
 - 图像多样性。尽量使用真实环境的图片，推荐来自一天中不同时间、不同季节、不同天气、不同照明、不同角度、不同来源（在线抓取、本地收集、不同相机）等的图像
 - 标签一致性。所有图片中所有需检测的实例都需要标注，不能漏标
 - 标签准确性。标签必须紧紧地包围每个对象。对象与其边界框之间不应存在空间。

###### labelImg使用快捷键
- w 创建区块,框选标注的物体,输入标签名称
- a/d 切换上一张/下一张
- 选中标签,可拖动或修改大小,右侧“编辑标签”可改变标签名称
- ctrl + d 复制当前标签
- ↑↓←→键 微调标签位置
- ctrl + v 复制上一张图片的标签 (在连续标注相同类别标签时很有用)

###### 标注数据注意事项
- 标注后会生成classes.txt文件,里面的顺序应和标注文件内的物体一一对应
- 第一次出现的物体要注意名称不要打错
- 多人合作标注一定要保证classes.txt内的顺序一致
- 标注框应紧贴被标注的物体,不要留有缝隙
- 注意不要漏标
