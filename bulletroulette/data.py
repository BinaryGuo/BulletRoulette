# 此文件用于定义各种常量。
from os.path import dirname

ASSET       = f"{dirname(__file__)}/asset/" # 存放图片背景音乐等素材的目录
LOCALE        = f"{dirname(__file__)}/locale/" # 存放翻译文件的路径
RED           = (255,  0,  0) # 红色RGB
WHITE         = (255,255,255) # 白色RGB
BACKGROUND    = f"{ASSET}bg.png" # 背景图
BGM           = f"{ASSET}bgm.ogg" # 背景音乐
FONT          = f"{ASSET}Simhei.ttf" # 字体
LETTERS       = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z") # 字母表
DELETE        = f"{ASSET}DELETE.png" # DELETE键
ENTER         = f"{ASSET}ENTER.png" # ENTER键
CHARGE        = f"{ASSET}charge.png" # 电量
GUN           = f"{ASSET}gun.png" # 枪（轮廓）
BLANKMUSIC    = f"{ASSET}blank.wav" # 射出空弹音效
LIVEDEALER    = f"{ASSET}livedealer.wav" # 大哥被打到时的音效
LIVEPLAYER    = f"{ASSET}liveplayer.wav" # 玩家被打到时的音效
BLANK         = f"{ASSET}blank.png" # 空弹
LIVEROUND     = f"{ASSET}liveround.png" # 实弹
SHOOTSELF     = f"{ASSET}dealershootself.png" # 大哥紫砂
SHOOTPLAYER   = f"{ASSET}dealershootplayer.png" # 大哥打玩家
SMOKE         = f"{ASSET}smoke.png"
HANDCUFF      = f"{ASSET}handcuff.png"
MAGNIFIER     = f"{ASSET}magnifier.png"
KNIFE         = f"{ASSET}knife.png"
PROPBOX       = f"{ASSET}propbox.png"
BEER          = f"{ASSET}beer.png"
PILL          = f"{ASSET}pill.png"
NONEPROP      = f"{ASSET}noneprop.png"
USESMOKE      = f"{ASSET}usesmoke.png"
USEKNIFE      = f"{ASSET}useknife.png"
USEHANDCUFF   = f"{ASSET}usehandcuff.png"
USEBEER       = f"{ASSET}usebeer.png"
USEMAGNIFIER  = f"{ASSET}usemagnifier.png"
DUSESMOKE     = f"{ASSET}dusesmoke.png"
DUSEKNIFE     = f"{ASSET}duseknife.png"
DUSEHANDCUFF  = f"{ASSET}dusehandcuff.png"
DUSEBEER      = f"{ASSET}dusebeer.png"
DUSEMAGNIFIER = f"{ASSET}dusemagnifier.png"
SEEBLANK      = f"{ASSET}seeblank.png"
SEELIVEROUND  = f"{ASSET}seeliveround.png"
BOOM          = f"{ASSET}boom.png"
HEALTH        = (2,4,6)
BULLETS = [ # 子弹（1代表实，0代表空）
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
            [1,1,1,1,1,1,0,0],
            [1,1,1,1,0,0,0,0],
            [1,1,0,0,0,0,0,0]
        ]
    ]
LETTERSPATH = [ASSET + l + ".png" for l in LETTERS]