import pygame
from plane_spites import *


#增加精灵和精灵组 敌机精灵的创建  敌机动画的效果


#屏幕大小的常量
SCREEN_WIDTH = 480
SCREEN_HEIGHY = 700
SCREEN_RECT = pygame.Rect(0,0,480,700)
CLOCK = 60

#游戏初始化
pygame.init()
screen = pygame.display.set_mode((480,700))
pygame.display.set_caption("BAll")

#绘制背景图像# 1> 加载图像
bg = pygame.image.load("../../images/background.png")
hero = pygame.image.load("../../images/me1.png")
#绘制在屏幕
screen.blit(bg, (0, 0))
#更新显示
pygame.display.update()
clock  = pygame.time.Clock()
hero_rect = pygame.Rect(150,300,102,126)  # x  y  width height

#222222222222222222222222222222222222222222222222
#22创建敌机的精灵
enemy = GameSprite("../../images/enemy1.png")
enemy1 = GameSprite("../../images/enemy1.png",2)
# 22创建敌机的精灵组
enemy_group = pygame.sprite.Group(enemy,enemy1)

# 游戏循环 意味着游戏正式开始
while True:
    clock.tick(60)
    # 捕捉事件
    # event_list = pygame.event.get()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # 卸载所有的模块
            exit()  # 直接终止当前正在执行的程序
    # 修改飞机的位置
    hero_rect.y -= 2
    # 判断飞机的位置
    if hero_rect.y<=0:
        hero_rect.y = 700
    # 调用blit方法绘制图像
    screen.blit(bg, (0, 0))

    screen.blit(hero, hero_rect)

    # 22 让精灵组调用两个方法
    # update  draw
    enemy_group.update()   # 让组中的所有精灵都更新位置
    enemy_group.draw(screen)  # 在screen上绘制所有的精灵

    # 调用update方法更新显示
    pygame.display.update()

pygame.quit()