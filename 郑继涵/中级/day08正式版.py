import pygame
import sys
import random

# 这节课主要内容是添加了分数和生命值   改变小球的方向

pygame.init()
screen = pygame.display.set_mode((640,700))
pygame.display.set_caption("BAll")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

ball_x = 110
ball_y = 100

rect_x = 300
rect_y = 650

speed = 10
speedx = speed
speedy = speed
clock = pygame.time.Clock()  # 设置时钟
font1 = pygame.font.Font(None, 24)

def print_text(scr, font, x, y, text, color = (250, 25, 255)):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x, y))

lives = 3
score = 0

while True:
    print(ball_y)
    clock.tick(60)  # 每秒执行60次
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((255,255,255))
    print_text(screen, font1, 0, 0, '命数:' + str(lives))
    print_text(screen, font1, 500, 0, '分数:' + str(score))
    ball_y += speedy
    ball_x += speedx


    if ball_y > 700:  #   球超过屏幕
        ball_y = -30
        ball_x = random.randint(20, 480)

    if ball_y < 0 and speedy<0:  #   球超过屏幕
        # speedx = -speedx
        speedy = -speedy

    if ball_x<30or ball_x>610:   # 检查左右边缘
        speedx = -speedx

    if ball_y > 650-30:              # 检查挡板是否借住
        if ball_x > rect_x and ball_x < rect_x + 200:
            speedx = -speedx
            speedy = -speedy

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        rect_x -= 5
    if keys[pygame.K_RIGHT]:
        rect_x += 5

    if rect_x > 640 - 100:
        rect_x = 640 - 100
    if rect_x < 0:
        rect_x = 0
    pygame.draw.circle(screen, (100, 40, 30), (ball_x, ball_y), 30, 0)
    pygame.draw.rect(screen, (0, 0, 255),(rect_x, rect_y, 200, 30))  # 其中第一个元组(x, y)表示的是该矩形左上角的坐标，第二个元组 (width, height)表示的是矩形的宽度和高度。

    pygame.display.update()  # 刷新屏幕内容显示
pygame.quit()  # 退出pygame