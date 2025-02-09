# Bullet Roulette 说明

## 特别说明

从此版本开始将：
- 停止对CLI界面的支持，但在以后的版本的CLIold.run函数中可以玩到1.1.2的CLI。
- 停止对pygame2.5.0以下版本的支持。

## 项目名称
- Bullet_Roulette

## 项目信息
- 此项目旨在将游戏“恶魔轮盘”的玩法移植到Python3上
- github：https://github.com/BinaryGuo/Bullet_Roulette/
- 问题反馈：https://github.com/BinaryGuo/Bullet_Roulette/issues/
- 联系邮箱（GQX）：kill114514251@outlook.com
- testPyPI：同名

## 版本
- 1.1.2

## 开发环境
- Ubuntu Linux 24.04
- Python 3.12.3
- Pygame 2.5.2

## 使用语言
- Python

## 改动说明

### 1.0（上个版本）
- 增加两个回合
- 增加图形界面（pygame）

### 1.1（此版本）
- 增加道具
- 增加开发者模式
- 新增英文版

### 1.2（计划）
- 增加PVP

### 1.3（计划）
- 增加开场
- 增加无尽模式

### 1.4（计划）
- 增加远程连接

### 1.5（计划）
- 增加多人模式

### 修复中BUG
- BUG1 在高帧率下的高灵敏度
- BUG2 增加获取屏幕尺寸功能
- METHOD1 打出子弹时显示子弹类型

## 项目说明

### 安装方法
在shell中输入：
> python3 -m pip install bulletroulette

或（前者更为保险）
> pip3 install bulletroulette

### 运行方法
启动IDLE
- 图形界面(GUI)：
> \>>> from bulletroulette.runGUI import run  
> \>>> run(CHEAT = True) # 作弊(显示子弹顺序)  
> \>>> run() # 正常游玩(FPS=15)  
> \>>> run(FPS = n) # n为正整数  
- shell界面(CLI旧版，不建议)：
> \>>> from bulletroulette.CLIold import run
> \>>> run(CHEAT = True) # 作弊(显示子弹顺序)  
> \>>> run() # 正常游玩  
- 开发者界面(其实就是README和LICENSE)：
> \>>> from bulletroulette.dev import run
> \>>> run()
> (roulette)>>> license()  # 协议
> (roulette)>>> readme()  # README
> (roulette)>>> exit()  # 退出

### 目录结构（在bulletroulette下）
```
/
    __init__.py
    CLIold.py
    data.py
    dev.py
    runCLI.py
    runGUI.py
    sprites.py
    locale/
        en/
            LC_MESSAGES/
                trans.po
                trans.mo
        ja/
            LC_MESSAGES/
                trans.po
    assets/
        A.png
        B.png
        C.png
        bgmsc.ogg
        blank.wav
        .
        .
        .
        (素材若干)
```

### 使用方法（游戏规则）

#### 窗口模式
1. 运行GUI后会弹出一个窗口，让您输入名称（鼠标）
2. 设置好名称后正式进入游戏，游戏分为三轮，每轮结束后会弹出 <您的名字> WIN!（在您赢的情况下），每一轮有若干发子弹，显示一次子弹为一小轮
3. 每一轮会先显示子弹（红色为实弹，灰色为空弹），显示后子弹顺序会被打乱
4. 每一小轮都是玩家先手，用鼠标选择枪后可点击DEALER射击对面，点击自己名字射击自己（左边为您和对面的血量）
5. 如果您选择射击对面，不管是空弹还是实弹，下一回合都是对面开枪。如果您选择射击自己，如果是实弹下一回合就该对面开枪，如果是空弹，下一回合还是您射击。（如果是实弹会听到“砰！”，如果是空弹会听到“咔...”）

#### 壳程序模式
1. 在选择壳程序模式后，会提示您输入名称
2. 在名称输入完成后正式进入游戏，游戏分为三轮，每轮结束后会弹出“恶魔死了！！！”（在您赢的情况下），每一轮有若干发子弹，显示一次子弹为一小轮
4. 每一轮会先显示枪膛里有几发子弹，显示后子弹顺序会被打乱。
5. 每一小轮都是玩家先手，输入一射击对面，点击自己名字射击自己（左边为您和对面的血量）
6. 如果您选择射击对面，不管是空弹还是实弹，下一回合都是对面开枪。如果您选择射击自己，如果是实弹下一回合就该对面开枪，如果是空弹，下一回合还是您射击。（如果是实弹会听到“砰！”，如果是空弹会听到“咔...”）

## 问题解决

### 找不到版本（安装问题）
> ERROR: Could not find a version that satisfies the requirement bulletroulette (from versions: none)  
> ERROR: No matching distribution found for bulletroulette

原因：Python版本小于3.8  
解决办法：重装一个Python3.8以上的版本

### 如果您的版本为1.0开头，并不是1.0.4的话请立即更新（1.0.4解决了很多问题）（如果不是WINDOWS，1.0.3也行）

## 鸣谢

### 测试人员

- 言邵阳（真名）  
- 陈晨（真名）  

## 格式规范
- GQXstd-readme 1.0 Independent