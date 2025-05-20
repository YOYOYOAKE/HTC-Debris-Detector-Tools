# HTC-Debris-Detector-Tools

此仓库存储我在 HTC-Debris-Detector 项目中用到的一些小工具。

| 工具 | 用途 |
| :--: | :--: |
| devider.py | 将图像与标签划分为训练集和验证集|
| labelme2yolo.py | 将 labelme 的 JSON 格式文件转换为 YOLO 实例分割任务的 txt 格式文件 | 

## divider.py 

需要以下目录结构：

```
- 项目文件夹
  - divider.py
  - images [图片文件夹]
    - xxx.jpg
    - ...
  - labels [标签文件夹]
    - xxx.txt
    - ...
  - dataset [工具生成的数据集文件夹（自动生成）]
```

进入项目文件夹执行`python divider.py`即可。

## labelme2yolo.py

需要安装依赖`pillow`。

需要以下目录结构：

```
- 项目文件夹
  - labelme2yolo.py
  - images [图片文件夹]
    - xxx.jpg
    - ...
  - jsons [labelme 生成的标注文件夹]
    - xxx.json
    - ...
  - labels [工具生成的 txt 文件夹（自动生成）]
```

进入项目文件夹执行`python labelme2yolo.py`即可。