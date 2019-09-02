import pygame
from 郑继涵.高级.plane_spritessss import *

#这次课主要类容是创建敌机  使用定时器创建敌机(1.设置事件id  2. 设置定时器   3. 监听事件)
# 2英雄飞机登场   通过按键来移动飞机

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
        self.__creat_sprints()

        # 设置定时器事件  敌机出现  1s
        pygame.time.set_timer(CREAT_ENEMY,1000)


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

    # 事件监听
    def __event_listen(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlainGame.__game_over()
            elif event.type == CREAT_ENEMY:
                print("敌机出厂")
                # 创建敌机精灵
                enemy = Enemy()
                # 将敌机的精灵添加到敌机精灵组
                self.enemy_group.add(enemy)
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            #     print("向右移动...")
        # 使用键盘提供的方法获取键盘事件 ---返会的是元组
        keys_pressed = pygame.key.get_pressed()
        # 判断元组中对应的按键索引值
        if keys_pressed[pygame.K_RIGHT]:
            self.hero.speed = 2
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -2
        else:
            self.hero.speed = 0

    # 碰撞检测
    def __check_collide(self):
        pass
    # 创建精灵
    def __creat_sprints(self):
        # 创建背景精灵和背景精灵组
        # bg1 = Background("../../images/background.png")
        # bg2 = Background("../../images/background.png")
        # bg2.rect.y = -bg2.rect.height
        bg1 = Background()
        bg2 = Background(True)
        self.back_group = pygame.sprite.Group(bg1,bg2)

        # 创建敌机的精灵组
        self.enemy_group = pygame.sprite.Group()

        # 创建英雄的精灵和精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    # 更新精灵
    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)

        # 更新敌机
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        # 更新英雄
        self.hero_group.update()
        self.hero_group.draw(self.screen)

    @staticmethod   # 没有使用类属性和对象的属性
    def __game_over():
        print("游戏结束")
        pygame.quit()
        exit()


if __name__ == '__main__':
    # 创建游戏对象
    game = PlainGame()
    game.start_game()