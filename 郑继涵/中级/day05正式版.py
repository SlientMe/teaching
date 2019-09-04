import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("BAll")
ball_x = 110
ball_y = 100
clock = pygame.time.Clock()  # 设置时钟
while True:
    clock.tick(60)  # 每秒执行60次
    for event in pygame.event.get():
        print(event.type)
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            ball_x += 1
            print("向右移动...")
    screen.fill((255,255,255))
    pygame.draw.circle(screen,(100, 40, 30),(ball_x, ball_y), 30, 0)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN]:
        ball_y += 1
    if keys[pygame.K_UP]:
        ball_y -= 1
    if keys[pygame.K_LEFT]:
        ball_x -= 1
    if keys[pygame.K_RIGHT]:
        ball_x += 1
    pygame.display.update()  # 刷新屏幕内容显示
pygame.quit()  # 退出pygame