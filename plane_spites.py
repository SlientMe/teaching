# -*- coding: utf-8 -*-
# @Time : 2019/7/10 11:14
# @Author : 刘琦
# @FileName: plane_spites.py
# @Software: PyCharm
import random
import pygame

# 创建敌机的定时器常量
CREAT_ENEMY_EVENT = pygame.USEREVENT

# 英雄发射子弹事件
HERO_FIRE_EVENT = pygame.USEREVENT + 1

SCREEN_RECT = pygame.Rect(0,0,480,700)


class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image_name, speed=1):
        super().__init__()
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self, *args):
        self.rect.y += self.speed

class Backgroud(GameSprite):
    def __init__(self,isalt= False):
        super().__init__("./images/background.png")
        if isalt:
            self.rect.y = -self.rect.height


    def update(self):
        super().update()
        if self.rect.y>= SCREEN_RECT.height:
            self.rect.y = -self.rect.height

class Enemy(GameSprite):
    def __init__(self):
        super().__init__("./images/enemy1.png")

        # 指定敌机的初始速度
        self.speed = random.randint(1,3)
        # 指定敌机的初始随机位置
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width -self.rect.width
        self.rect.x = random.randint(0,max_x)

    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            # print("飞出屏幕")
            self.kill()

    def __del__(self):
        print("d敌机挂了")

class Hero(GameSprite):
    """英雄精灵"""
    def __init__(self):
        super().__init__("./images/me1.png",0)
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom-120

        #创建子弹的精灵组
        self.bullets = pygame.sprite.Group()

    def update(self):
        self.rect.x += self.speed

        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right>SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):
        print("发射子弹")
        # 创建子弹精灵
        for i in (0,1,2):
            bullet = Bullt()
            bullet.rect.bottom = self.rect.y-i*20
            bullet.rect.centerx = self.rect.centerx

            self.bullets.add(bullet)

class Bullt(GameSprite):
    """子弹精灵"""
    def __init__(self):
        super().__init__("./images/bullet1.png",-2)

    def update(self):
        super().update()
        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        print("子弹被销毁")

