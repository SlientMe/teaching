import pygame
import sys

# 绘制背景图像# 1> 加载图像
# bg = pygame.image.load("./images/background.png")
# 绘制在屏幕
# screen.blit(bg, (0, 0))
# 更新显示
# pygame.display.update()

pygame.init()  # 初始化pygame
screen = pygame.display.set_mode((640, 480))  # 设置窗口大小 显示窗口
pygame.display.set_caption('BALL')
ball_x = 110
ball_y = 100
# circle = pygame.

while True:  # 死循环确保窗口一直显示
    for event in pygame.event.get():  # 遍历所有事件
        if event.type == pygame.QUIT:  # 如果单击关闭窗口，则退出
            sys.exit()
    screen.fill((0,0,0))  # 填充颜色(设置为0，执不执行这行代码都一样)
    pygame.draw.circle(screen,(100, 40, 30),(ball_x, ball_y), 30, 0)
    ball_y += 1
    pygame.display.update()     #刷新屏幕内容显示
pygame.quit()  # 退出pygame

#
# ball = pygame.image.load('ball.jpg').convert()
# rect = pygame.image.load('木板.jpg').convert()
# newRect = pygame.transform.scale(rect, (100, 20))
# newBall = pygame.transform.scale(ball, (50,50))
# key_x = 450
# x = 10
# y = 10
# speedx = 1
# speedy = 1
# while True:
#     screen.fill((255,255,255))
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()
#         # if event.type == pygame.KEYDOWN:
#         #     if event.key == pygame.K_LEFT:
#         #         key_x -= 1
#         #     if event.key == pygame.K_RIGHT:
#         #         key_x += 1
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_LEFT]:
#         key_x -= 1
#     if keys[pygame.K_RIGHT]:
#         key_x += 1
#     screen.blit(newBall, (x, y))
#     screen.blit(newRect, (key_x,480))
#
#     pygame.display.update()
