import pygame
import random
import math

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((600,400))
    screen.fill((255,255,255))
    # 设置窗口标题
    pygame.display.set_caption('大小乱舞')
    pygame.display.flip()
    # all_balls 保存多个球
    # 每个球要保存：半径，圆心坐标，颜色，x速度，y速度
    all_balls = []
    while True:
        # 刷新界面
        for event in pygame.event.get():
            # 不同类型的事件对应的type值不一样
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # 点一下鼠标创建一个球
                ball = {'r':random.randint(10,20),
                        'pos':event.pos,
                        'color':(random.randint(0,255),random.randint(0,255),random.randint(0,255)),
                        'x_speed':random.randint(-3,3),
                        'y_speed':random.randint(-3,3)}
                # 保存球
                all_balls.append(ball)
        # 清屏操作
        screen.fill((255, 255, 255))
        # 遍历小球
        for ball in all_balls:
            x,y = ball['pos']
            # 遍历其他球
            for o_ball in all_balls:
                o_x,o_y = o_ball['pos']
                # 如果两个球相撞
                if o_ball['pos'] != ball['pos'] and math.sqrt((x-o_x)**2+(y-o_y)**2) < (ball['r']+o_ball['r']):
                    # 球半径大的吸收半径小的，将小球销毁
                    if ball['r'] >= o_ball['r']:
                        ball['r'] += o_ball['r']
                        # 如果球的半径过大，将其销毁，改变为初始的任意球
                        if (x-ball['r']-math.fabs(ball['x_speed']) <= 0 or x+ball['r']+math.fabs(ball['x_speed']) >= 600) or (y-ball['r']-math.fabs(ball['y_speed']) <= 0 or y+ball['r']+math.fabs(ball['x_speed']) >= 400):
                            ball['r'] = random.randint(10,20)
                        all_balls.remove(o_ball)
            # 越界判断，越界改变方向轴速度
            if x-ball['r']-math.fabs(ball['x_speed']) <= 0 or x+ball['r']+math.fabs(ball['x_speed']) >= 600:
                ball['x_speed'] = 0 - ball['x_speed']
            if y-ball['r']-math.fabs(ball['y_speed']) <= 0 or y+ball['r']+math.fabs(ball['x_speed']) >= 400:
                ball['y_speed'] = 0 - ball['y_speed']
            x_speed = ball['x_speed']
            y_speed = ball['y_speed']
            x += x_speed
            y += y_speed
            pygame.draw.circle(screen,ball['color'],(x,y),ball['r'])
            # 更新球对应的坐标
            ball['pos'] = x,y
        pygame.time.delay(5)
        pygame.display.flip()
        # if event.type == pygame.MOUSEMOTION:
        #     print('鼠标移动',event.pos)