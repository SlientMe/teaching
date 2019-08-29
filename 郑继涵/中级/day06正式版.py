import pygame
import sys
import random

# 这节课主要内容是制作挡板的移动，让小球随机下落，改变速度 ， 最后显示文子

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

speed = 3
clock = pygame.time.Clock()  # 设置时钟
font1 = pygame.font.Font(None, 24)

def print_text(scr, font, x, y, text, color = (250, 25, 255)):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x, y))


while True:
    print(ball_y)
    clock.tick(60)  # 每秒执行60次
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # if event.type == pygame.MOUSEMOTION:
        #     rect_x = event.pos[0]
    screen.fill((255,255,255))
    imgText = font1.render('test text', True, (250, 25, 240))  # 文本，是否抗锯齿，颜色
    screen.blit(imgText, (200, 100))

    pygame.draw.circle(screen,(100, 40, 30),(ball_x, ball_y), 30, 0)
    pygame.draw.rect(screen, (0, 0, 255), (rect_x, rect_y, 100, 30))  # 其中第一个元组(x, y)表示的是该矩形左上角的坐标，第二个元组 (width, height)表示的是矩形的宽度和高度。
    ball_y += speed

    if ball_y > 700:
        ball_y = -20
        ball_x = random.randint(20, 480)

    keys = pygame.key.get_pressed()
    # if keys[pygame.K_DOWN]:
    #     ball_y += 1
    # if keys[pygame.K_UP]:
    #     ball_y -= 1
    # if keys[pygame.K_LEFT]:
    #     ball_x -= 1
    # if keys[pygame.K_RIGHT]:
    #     ball_x += 1
    if keys[pygame.K_LEFT]:
        rect_x -= 2
    if keys[pygame.K_RIGHT]:
        rect_x += 2

    if rect_x > 640 - 100:
        rect_x = 640 - 100
    if rect_x < 0:
        rect_x = 0

    pygame.display.update()  # 刷新屏幕内容显示
pygame.quit()  # 退出pygame