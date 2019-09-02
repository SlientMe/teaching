import pygame
from 郑继涵.高级.plane_spritessss import *

# 这节课主要是面向对象开发，搭建游戏的主框架

# 常量  -- 不可变化的量
# 变量 ---可变的量

class PlainGame(object):
    """飞机大战的主游戏"""
    def __init__(self):
        print("游戏初始化")
        # 创建游戏窗口
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN.size)
        pygame.display.set_caption("BAll")
        # 创建游戏时钟
        self.clock = pygame.time.Clock()
        # 调用私有方法，精灵和精灵组的创建
        self.__creat_sprites()


    def __creat_sprites(self):
        pass


    def start_game(self):
        print("开始游戏")
        while True:
            # 1. 设置刷新频率
            self.clock.tick(FPS)
            # 2. 事件监听
            self.__event_listen()
            # 3. 碰撞检测
            self.__check_collide()
            # 4. 更新、绘制精灵
            self.__update_sprites()
            # 5. 更新显示
            pygame.display.update()
            pass

    # 事件监听
    def __event_listen(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlainGame.__game_over()
        pass

    # 碰撞检测
    def __check_collide(self):
        pass
    # 创建精灵
    def __creat_sprints(self):
        pass

    # 更新精灵
    def __update_sprites(self):
        pass

    @staticmethod   # 没有使用类属性和对象的属性
    def __game_over():
        print("游戏结束")
        pygame.quit()
        exit()


if __name__ == '__main__':
    # 创建游戏对象
    game = PlainGame()
    game.start_game()