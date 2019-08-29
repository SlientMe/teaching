# 导入库一般要在最上面
import pygame
import random

# 函数
def ball():
    # 初始化
    pygame.init()
    # 设置界面，界面要保存在一个界面里
    screen = pygame.display.set_mode([800, 600])
    # 设置标题
    pygame.display.set_caption("ball")
    running = True
    ball_x = 100
    ball_y = 200
    rect_x = 600
    rect_y = 500
    rect_w = 130
    rect_h = 30
    scores = 0
    lives = 3
    # 游戏的主循环 （游戏中的操作和画面变化都在主循环里）
    while running:
        # 事件循环
        for event in pygame.event.get():  # 得到全部事件：我们的所有操作都叫做事件
            # type类型
            if event.type == pygame.QUIT:  # QUIT指的是退出事件
                running = False  # running变量
            # 如果是鼠标移动事件MOUSEMOTION，更改挡板坐标rect_x，rect_y，鼠标位置evnet.pos
            if event.type == pygame.MOUSEMOTION:
                rect_x, rect_y = event.pos  # 事件坐标position
        screen.fill([255, 255, 255])
        # 画小球（界面的变量，颜色RGB颜色表示法，坐标，半径，0)
        pygame.draw.circle(screen, (255, 255, 0), (ball_x, ball_y), 30, 0)
        # 画挡板(界面，颜色，坐标和长宽，0)
        pygame.draw.rect(screen, (0, 0, 0), (rect_x, rect_y, rect_w, rect_h), 0)
        # 刷新界面(界面上de图形发生变化后，用update刷新，画面才能显示出来)
        pygame.display.update()
        ball_y = ball_y + 1
        if 0 < rect_y - ball_y <= 30 and rect_x < ball_x < rect_x + rect_w:
            ball_y = 0
            ball_x = random.randint(30,770)
            scores = scores + 1
        elif ball_y>630:
            ball_y = 0
            ball_x = random.randint(30, 770)
            lives = lives - 1
        pygame.time.delay(5)

ball()
