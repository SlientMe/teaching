import pygame
import random

pygame.init()#初始化

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('接小球游戏')
clock = pygame.time.Clock()
RED = 255, 0, 0
GREEN = 0, 255, 0
BLUE = 0, 0, 255
BLACK = 0, 0, 0
WHITE = 255, 255, 255
ballx = 100
bally = 0
rx = 400
ry = 560
rw = 200
rh = 30
live = 3
vy = 1
score = 0
color = RED
font = pygame.font.Font('simhei.ttf', 50)#定义一段字体  1
def write(content, x, y, color=WHITE):
    text = font.render(content, True, color)#渲染一段文字  2
    screen.blit(text, (x, y))#将渲染的文字贴到屏幕上  3
while True:
    screen.fill(BLACK)
    # clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEMOTION:
            rx = event.pos[0] - rw // 2
    write('生命:' + str(live), 0, 0, )
    write('分数:' + str(score), 640, 0)
    pygame.draw.circle(screen, color, (ballx, bally), 30)
    pygame.draw.rect(screen, GREEN, (rx, ry, rw, rh))
    bally += 1
    if bally >= 600:
        bally = 0
        ballx = random.randint(0, 800)
        live -= 1
    elif bally + 30 > ry and rx < ballx < rx + rw:
        bally = 0
        ballx = random.randint(0, 800)
        score += 1
        color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        # vy += 1
    elif rx + rw >= 800:
        rx = 800 - rw
    elif rx <= 0:
        rx = 0

    pygame.display.update()
