# Fate-Grand-Order-AnJianJingLing-Script
## Fate Grand Order Auto Battle Script / AnJianJingLing Mobile Helper Script

### 按键精灵手机助手 FGO自动战斗脚本

可选安卓模拟器：最新版雷电，最新版逍遥安卓(android 5.1 image)。设置长1080，宽1920，dpi288

启动按键精灵安卓版与fgo后，请手动翻转屏幕2次（即180°旋转）。库函数用途多在函数定义处有描述。

常用附件：cardok.png、zhi.png、blue/red/green.png、Next.png、UseItem.png、特定从者\礼装组合的助战识别用图

> PS：按键精灵手机助手是IDE，按键精灵安卓版是脚本执行器，与按键精灵PC版几乎没有任何关系

Android Simulator: ldplayer, MEMU(use its android 5.1 image). set length=1080, width=1920, dpi=288. (phone simulation)

when AnJianJingLing in Android and FGO are ready, Flip the screen of the Android Simulator 180° by using its side buttons.

The process of current latest \[Lib\] script: Tap, select assistant servant, start battle, Only Use Cards in Stage 1&2, Use 3 NPs only in Stage3.

useful attachments: cardok.png(Function Wait4OK), zhi.png(Function Advantage)、blue/red/green.png(recognize card color)、Next.png(confirm a battle)、UseItem.png(whether to eat apples)

------------
Update Since 2022 (2023-04-04)

+ for latest Simplified Chinese FGO 30fps
+ Select support servants from EXTRA class (Oberon!)
+ add Function: ChangeTeam(t) t=1,2,...,10; select team before battle
+ add Function: getHPpercent(SvtPos) SvtPos=1,2,3; Binary search!
+ UI for instant control: support, questType(free21ap free22ap event40ap Yellow20ap), loop times, apple type, team No..


Update On 2021-12-25

+ Compatible for latest Simplified Chinese FGO 120fps version.
+ add Function: LeastDamage


Update On 2020-10-19

+ Compatible for latest Simplified Chinese FGO(V2.61).
+ NO NEED for getting color from skills each time when making a new scipt! just add cardok.jpg in scipts, and use Function:Wait4OK instead of Function:Wait4NextOperation!
+ add switch for Function:FocusOn, to control whether to change target to kill. (parameter forced=1, never change; forced=0, automatically change if cards no so good)

Update On 2019-11-08

+ New FGO(V1.55), New branch. 
+ Compatible for severe Simplified Chinese FGO.
+ Implement & bugfix "Advantage", which can use "克制"(kezhi) cards as much as possible without user's extra snapshot.

Update On 2019-10-26
+ Add FocusOn, which can arrange normal attack more reasonable on some enemies with more HPs. 
+ You should snap a Core Servant's Command Card Portrait and assign it to Variable: Core. 

Update On 2019-04-03
+ Adapt to FGO Client, Version 1.45.1

#### Legacy
----

Update from Oct.2017 to Dec.2018

based on FGO Chinese mainland server.

only use it when upper right corner of FGO screen is upeer left coner of your phone.
(that is, Turn 90 degrees clockwise when you start to play FGO if you want to use the script. )

select support as you like (take pictures of the support you want).

recognize buster arts quick cards, even some servants.

can use BBB/BAB/BQB .ect for more damage.

judge whether the script can do next operation. (use skill/use cards/skip friends application/Skip Essence Craft Drop(Only Star 5 Now))

in floder "pic4scripts", there're some useful pictures for your own script design.

eat apples in some exciting events and loop it around the clock!

PS: codes for "Using Critical Cards" are warmly welcomed!

