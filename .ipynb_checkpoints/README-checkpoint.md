# Buckshot Roulette 恶魔轮盘赌
## 版本
- 1.0


## 开发环境
- linux ubuntu 22.04（主要开发环境，负责运行代码等等）
- apple mac 14.0（主要是使用mac上自带的“预览”来测量图片并使用PIL.Image进行切割、缩放等操作）
其实ubuntu在网上也有测像素的工具，但我懒得找了......
正好家里有台mac，就选择用mac完成。


## 改动说明

### 0.1(上个版本)
- 使用类初步实现了游戏
- 可玩性不高

### 1.0
- 增加道具
- 增加两个回合
- 增加图形界面（pygame）

### debug
- 降低在高帧率下的高灵敏度问题
- 增加获取功能


## 程序说明
- 你可以看到在每个.py文件开头简短的说明
### 安装方法
在shell(Terminal(Mac/Linux)或cmd(Windows))
> python3 -m pip install bulletroulette

或（前者更为保险）
> pip3 install bulletroulette

### 运行方法
启动IDLE(shell输入python)
> \>>> from bulletroulette.run import run
> \>>> run()

(终止时需按下^C ^D)

### 目录结构（在/bulletroulette下）
/
    __init__.py  
    run.py  
    data.py  
    roles.py  
    sprites.py  
    assets/
        A.png  
        B.png
        C.png
        .
        .
        .
        X.png
        Y.png
        Z.png
        bgmsc.ogg
        blank.wav
        .
        .
        .
        (素材若干)


## 道歉
- 不好意思，此版本没有提供开发接口，README也写的不多，请见凉！
- 不好意思，由于之前upload比较匆忙，没来得及改README上的协议（CC-BY-SA 3.0），assets目录下还有个临时存放的二维码没有删，请见凉。


## 问题解决
### 找不到版本（安装问题）
> ERROR: Could not find a version that satisfies the requirement bulletroulette (from versions: none)
> ERROR: No matching distribution found for bulletroulette

原因：Python版本小于3.8
解决办法：重装一个Python3.8以上的版本