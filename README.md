# BiliDrive-Easy-Download
BiliDrive Easy Download is a Free software tool to Batch download bilibili files.
===========================

###########环境依赖



###########使用方法
1. 在Android手机的哔哩哔哩App中，把想要下载的视频，缓存在手机中。

2. 手机连接电脑，把缓存文件拷贝到电脑中。

3. 修改config.ini配置文件：
    eg: src_bili_path =  # 原始文件目录，即上一步骤拷贝到电脑中的目录
        det_bili_path =  # 生成文件目录，即转换好后的文件在电脑中的存放目录

4. 执行generate.py。
    eg: 在命令行中，进入到项目目录，执行python generate.py


##########


<h1 align="center">
  <br>
  BiliDrive-Easy-Download
  <br>
</h1>

[![LICENSE](https://github.com/davidhefan/BiliDrive-Easy-Download/blob/main/LICENSE)](LICENSE)

BiliDrive Easy Download is a Free software tool to Batch download bilibili files.

哔哩哔哩 (bilibili.com) 批量下载工具。很多网站可以下载单个文件，但是如果有几十个几百个文件，一个一个下载会是十分耗费精力和时间的一件事，本项目给出了一种批量下载哔哩哔哩的方法和工具。


## 使用方法

1. 在Android手机的哔哩哔哩App中，把想要下载的视频，缓存在手机中。

2. 手机连接电脑，把缓存文件拷贝到电脑中。

3. 修改config.ini配置文件：
    eg: src_bili_path =  # 原始文件目录，即上一步骤拷贝到电脑中的目录
        det_bili_path =  # 生成文件目录，即转换好后的文件在电脑中的存放目录

4. 执行generate.py。
    eg: 在命令行中，进入到项目目录，执行python generate.py

## 目录结构描述
├── Readme.md                   // 说明文件
├── generate.py                 // 执行文件
├── config.ini                  // 配置文件
└── utils                       // 工具
    ├── config_process.py       // 配置文件读取类
    ├── ffmpeg_utils.py         // 应用ffmpeg做音视频处理的工具类
    ├── moviepy_utils.py        // 应用moviepy做音视频处理的工具类
    └── myutils.py              // 文件处理类


## V1.0.0 版本内容更新
1. 实现手机缓存的视频文件，导入电脑后，批量转换为mp4格式文件。
