import sys

import pygame

from plane_spites import *

pygame.init()
#创建游戏窗口
screen = pygame.display.set_mode((480,700))

hero = pygame.image.load("./images/me1.png")
clock = pygame.time.Clock()

# 定义飞机的初始位置
hero_rect = pygame.Rect(150, 300, 102, 126)



while True:
    clock.tick(120)
    hero_rect.y -= 1
    if hero_rect.y <= 0:
        hero_rect.y =60
    # 监听事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("游戏退出...")
            pygame.quit()
            sys.exit()

    screen.blit(hero,hero_rect)



    #调用update更新显示
    pygame.display.update()



