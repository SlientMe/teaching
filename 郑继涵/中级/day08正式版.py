import pygame
import sys
import random

# 这节课主要内容是将屏幕上自己画的内容替换为图片。 添加背景图片

pygame.init()
screen = pygame.display.set_mode((640,700))
pygame.display.set_caption("BAll")

ball = pygame.image.load('./img/ball.png')  # 加载小球图片图片
sport = pygame.image.load('./img/sport.png')  # 添加挡板图片
bg = pygame.image.load('./img/background.png')  # 加载小球图片图片
ballrect = ball.get_rect()  # 获取矩形区域
sportrect = sport.get_rect()

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


sportrect.y = 650

speed = 5
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
    # print(ballrect.y)
    clock.tick(60)  # 每秒执行60次
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((255,255,255))
    # screen.blit(bg, (0, 0))   # 添加背景颜色。

    print_text(screen, font1, 0, 0, 'live:' + str(lives))
    print_text(screen, font1, 500, 0, 'socre:' + str(score))
    ballrect.y += speedy
    ballrect.x += speedx
    print(ballrect.x)


    if ballrect.y > 700:  #   球超过屏幕
        ballrect.y = -30
        ballrect.x = random.randint(20, 480)

    if ballrect.y < 0 and speedy<0:  #   球超过屏幕
        # speedx = -speedx
        speedy = -speedy

    if ballrect.x<30or ballrect.x>610:   # 检查左右边缘
        speedx = -speedx

    if ballrect.y > 650-30:              # 检查挡板是否借住
        if ballrect.x > sportrect.x and ballrect.x < sportrect.x + 200:
            speedx = -speedx
            speedy = -speedy

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        sportrect.x -= 5
    if keys[pygame.K_RIGHT]:
        sportrect.x += 5

    if sportrect.x > 640 - 100:
        sportrect.x = 640 - 100
    if sportrect.x < 0:
        sportrect.x = 0
    screen.blit(ball, ballrect)  # 将小球画在屏幕上
    screen.blit(sport, sportrect)  # 讲挡板画在屏幕上

    pygame.display.update()  # 刷新屏幕内容显示
pygame.quit()  # 退出pygame