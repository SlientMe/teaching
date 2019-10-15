# 游戏精灵的开发  主要是为主程序提供工具的类
import random
import pygame

# 屏幕大小的常量
SCREEN = pygame.Rect(0, 0, 480, 700)
FPS = 60
#创建敌机的定时器常量
CREAT_ENEMY = pygame.USEREVENT
# 英雄发射子弹的事件
HERO_FIRE = pygame.USEREVENT+1

class GameSprite(pygame.sprite.Sprite):
     """文档注释：飞机大战游戏精灵"""
     def __init__(self,image_name,speed=1):
         # 调用父类的初始化方法
         super().__init__()
         # 定义对象的属性
         self.image = pygame.image.load(image_name)
         self.rect = self.image.get_rect()
         self.speed = speed

     def update(self, *args):
         self.rect.y += self.speed

class Background(GameSprite):
    """游戏背景精灵"""

    def __init__(self,is_alt = False):
        # 1.调用父类方法实现精灵的创建（img/rect/speed）
        super().__init__("../../images/background.png")
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self, *args):
        # 1. 调用分类的方法实现
        super().update()
        # 2.判断是否移除屏幕
        if self.rect.y>=SCREEN.height:
            self.rect.y = -self.rect.height

class Enemy(GameSprite):
    """敌机精灵"""
    def __init__(self):
        # 1. 调用父类方法，创建敌机精灵，同时指定敌机图片
        super().__init__("../../images/enemy1.png")
        # 2.指定敌机初试速度
        self.speed = random.randint(1,3)

        # 3. 指定敌机随机位置
        self.rect.bottom = 0
        self.rect.x = random.randint(0,SCREEN.width-self.rect.width)

    def update(self, *args):
        # 1.调用父类方法
        super().update()
        # 2.判读是否飞出屏幕
        if self.rect.y >= SCREEN.height:
            print("飞出屏幕")
            self.kill()

    # 内置的方法，当调用kill时会被执行
    def __del__(self):
        print("敌机挂了")

class Hero(GameSprite):
    """英雄精灵"""
    def __init__(self):
        # 1.调用父类方法
        super().__init__("../../images/me1.png",0)
        # 2.设置英雄的初试位置
        self.rect.centerx  = SCREEN.centerx
        self.rect.bottom = SCREEN.bottom - 120

        # 3.创建子弹的精灵组
        self.bullets = pygame.sprite.Group()


    def update(self, *args):
         self.rect.x += self.speed
         if self.rect.x <0:
             self.rect = 0
         elif self.rect.right > SCREEN.width:
             self.rect.right = SCREEN.width

    def fire(self):
        print("fire")
        for i in (0,1,2):  # 创建多个子弹
            # 1创建子弹精灵
            bullet = Bullet()
            # 2设置精灵的位置
            bullet.rect.bottom = self.rect.y-20*i
            bullet.rect.centerx = self.rect.centerx
            # 3 将精灵添加到精灵组
            self.bullets.add(bullet)

class Bullet(GameSprite):
    """子弹精灵"""
    def __init__(self):
        # 1.调用父类方法
        super().__init__("../../images/bullet1.png",-2)

    def update(self, *args):
        # 调用父类方法 ，让子弹垂直飞行
        super().update()
        # 判断子弹是否飞出屏幕
        if self.rect.bottom<0:
            self.kill()

    def __del__(self):
        print("子弹被销毁")