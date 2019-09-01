import pygame
import sys

# 1.初始化pygame
pygame.init()
# 2. 设置窗口大小
screen = pygame.display.set_mode((640, 480))  # 设置窗口大小 显示窗口
width = 640
height = 480
# 3. 设置窗口名字
pygame.display.set_caption('BALL')

ball = pygame.image.load('./img/ball.png')  # 加载图片
ballrect = ball.get_rect()  # 获取矩形区域


# ballrect = pygame.Rect(0, 0, 16, 16)  # pygame.Rect(left, top, width, height)


speed = [1, 1]  # 设置移动的X轴、Y轴

clock = pygame.time.Clock()  # 设置时钟


while True:  # 死循环确保窗口一直显示
    clock.tick(60)  # 每秒执行60次

    for event in pygame.event.get():  # 遍历所有事件
        if event.type == pygame.QUIT:  # 如果单击关闭窗口，则退出
            sys.exit()
    ballrect = ballrect.move(speed)  # 移动小球

    # 碰到左右边缘
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    # 碰到上下边缘
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill((0,0,0))  # 填充颜色(设置为0，执不执行这行代码都一样)
    screen.blit(ball, ballrect)  # 将图片画到窗口上
    pygame.display.update()  # 更新全部显示



pygame.quit()  # 退出pygame