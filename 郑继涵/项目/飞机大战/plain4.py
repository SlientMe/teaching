from 郑继涵.项目.飞机大战.plane_spritessss import *

#这次课首先是让背景图片滚动效果,设计一个背景类

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
        pass

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

    # 更新精灵
    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)

    @staticmethod   # 没有使用类属性和对象的属性
    def __game_over():
        print("游戏结束")
        pygame.quit()
        exit()


if __name__ == '__main__':
    # 创建游戏对象
    game = PlainGame()
    game.start_game()