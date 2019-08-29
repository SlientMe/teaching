# -*- coding: utf-8 -*-
# @Time : 2019/7/12 6:10
# @Author : liuqi
# @FileName: main.py
# @Software: PyCharm

import pygame
from plane_spites import *

#屏幕大小的常量
SCREEN_WIDTH = 480
SCREEN_HEIGHY = 700
SCREEN_RECT = pygame.Rect(0,0,480,700)
CLOCK = 60

class PlainGmage(object):
    def __init__(self):
        print("游戏初始化")
        # 创建游戏的窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        #创建游戏时钟
        self.clock = pygame.time.Clock()
        #调用石油方法，精灵和精灵组的创建
        self.__creat_sprints()

        # 设置定时器事件 创建敌机
        pygame.time.set_timer(CREAT_ENEMY_EVENT, 1000)
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)

    def start_game(self):
        print("游戏开始")
        while True:
            # 1设置刷新频率
            self.clock.tick(CLOCK)
            # 2事件监听
            self.__event_handle()
            # 3.碰撞检测
            self.__check_collide()
            # 4更新精灵
            self.__update_sprites()
            # 5更新显示
            pygame.display.update()

    def __event_handle(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlainGmage.__game_over()
            elif event.type == CREAT_ENEMY_EVENT:
                # print("敌机出场")
                ememy = Enemy()
                self.enemy_group.add(ememy)
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            #     print("向右移动...")
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()

        # 使用键盘提供的方法获取键盘按键
        keys_press = pygame.key.get_pressed()
        if keys_press[pygame.K_RIGHT]:
            self.hero.speed = 2
        elif keys_press[pygame.K_LEFT]:
            self.hero.speed = -2
        else:
            self.hero.speed = 0


    def __check_collide(self):
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)

        enemies = pygame.sprite.spritecollide(self.hero,self.enemy_group,True)

        if len(enemies) > 0:
            self.hero.kill()
            PlainGmage.__game_over()

    def __creat_sprints(self):

        #背景精灵和精灵组
        bg1 = Backgroud()
        bg2 = Backgroud(True)
        self.back_group = pygame.sprite.Group(bg1, bg2)

        #创建敌机的精灵和精灵组
        self.enemy_group = pygame.sprite.Group()

        #创建英雄的精灵和精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    @staticmethod
    def __game_over():
        pygame.quit()
        exit()

if __name__ == '__main__':
    #创建游戏对象
    plaingame = PlainGmage()
    #启动程序
    plaingame.start_game()