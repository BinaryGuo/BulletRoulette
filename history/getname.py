__version__ = "1.0"
# 恶魔轮盘赌
# Levolet Inc.
# CC-BY-SA 3.0

# 外部导入
from random import shuffle
from time import sleep
import pygame
from traceback import print_exc
from os import chdir,getcwd
# 模块导入
from roles import *
from data import *
from sprites import Button
# 以下是主程序
chdir(DIR)
print(getcwd())
health = [2,4,6]
buckshots = [ # 子弹（1代表实，0代表空）
        [
            [1,0,0],
            [1,1,0,0]
        ],
        [
            [1,0],
            [1,1,0,0,0],
            [1,1,1,0,0,0],
            [1,1,1,1,0,0,0,0]
        ],
        [
            [1,1,1,1,1,0,0,0],
            [1,1,1,1,0,0,0,0],
            [1,1,1,0],
            [1,1,1,1,0,0,0,0]
        ]
    ]
try:
    mode = int(input("请选择模式（窗口按1（游戏体验更好）,壳程序按2（更为稳定））:"))
    if mode == 1:
        FPS = int(input("请设置帧率（如果设的太高您的计算机可能运行不了，区间：1～200）："))
        pygame.init()
        # 以下是一些关于pygame的一些常量声明
        # 以下是初始化
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((1400,850))
        pygame.display.set_caption("Buckshot Roulette")
        background = pygame.image.load(BACKGROUND)
        backgroundmusic = pygame.mixer.Sound(BGM)
        text = pygame.font.Font(FONT,50)
        nametext = text.render("Enter name:",False,WHITE)
        nametextlocation = nametext.get_rect()
        nametextlocation.center = (700,100)
        buttons = []
        name = ""
        for i in range(26):buttons.append(Button(50*(i+1),700,pygame.image.load(f"assets/{LETTERS[i]}.png"),1))
        delete = Button(500,760,pygame.image.load(DELETE),1)
        enter = Button(900,760,pygame.image.load(ENTER),1)
        # 以下是一些控制变量
        done = False # 结束
        naming = True # 正在命名
        playerturn = False # 玩家回合
        dealerturn = False # 恶魔回合
        # 以下是游戏主循环
        backgroundmusic.play()
        while not done:
            screen.blit(background,(-50,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("QUIT")
                    done = True
            if naming:
                screen.blit(nametext,nametextlocation)
                for i in buttons: 
                    if i.run(screen) == 1:
                        name += (LETTERS[buttons.index(i)])
                if delete.run(screen) == 1:
                    name = name.rstrip(name[-1])
                if enter.run(screen) == 1:
                    naming = False
                tmpnametext = text.render(name,False,WHITE)
                tmpnametextlocation = tmpnametext.get_rect()
                tmpnametextlocation.center = (700,400)
                screen.blit(tmpnametext,tmpnametextlocation)
            else:
                print(name)
                done = True
            pygame.display.update()
            clock.tick(FPS)
        backgroundmusic.stop()
        pygame.quit()
    else:
        name = input("你的名字：")
        for j in range(3):
            dealer = Dealer(health[j])
            player = Player(health[j],name)
            for i in range(len(buckshots[j])):
                buckshot = buckshots[j][i]
                buckshotcount = [0,0]
                for k in buckshot:
                    if k == 1:buckshotcount[0]+=1
                for k in buckshot:
                    if k == 0:buckshotcount[1]+=1
                next = 0
                shuffle(buckshot)
                print(f"{buckshotcount[0]}发实弹，{buckshotcount[1]}发空弹")
                for i in range(len(buckshot)):
                    print(f"恶魔血量:{dealer.gethealth()} {name}的血量:{player.gethealth()}")
                    if next == 0:
                        if player.shoot() == 1:
                            if buckshot[i] == 1:
                                print("砰！！！")
                                dealer.hurt()
                            else:
                                print("咔......")
                            next = 1
                        else:
                            if buckshot[i] == 1:
                                print("砰！！！")
                                player.hurt()
                                next = 1
                            else:
                                print("咔......")
                    else:
                        if dealer.shoot() == 1:
                            print(f"恶魔选择向{name}开枪！！！")
                            if buckshot[i] == 1:
                                print("砰！！！")
                                player.hurt()
                            else:
                                print("咔......")
                            next = 0
                        else:
                            print("恶魔选择向自己开枪......")
                            if buckshot[i] == 1:
                                print("砰！！！")
                                dealer.hurt()
                                next = 0
                            else:
                                print("咔......")
                    if dealer.gethealth() == 0 or player.gethealth() == 0:exit()
                    sleep(1.5)
            del dealer
            del player
except KeyboardInterrupt:
    print("\n检测到^C")
    exit()
except SystemExit:pass
except:
    print("抱歉，我们检测到了一个错误，这可能不是您造成的，但您无法继续进行游戏了")
    print("错误信息：")
    print_exc()
print("游戏结束!")
print("感谢您的游玩!")
print("名称:Buckshot Roulette（恶魔轮盘赌）")
print("版本：1.0")
print("LevoLet Inc.")