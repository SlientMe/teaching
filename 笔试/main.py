# -*- coding: utf-8 -*-
# @Time : 2019/7/9 10:25
# @Author : 刘琦
# @FileName: main.py
# @Software: PyCharm

import os
import sys
import random
import time
import pygame
from pygame.locals import *
from 笔试.typeUtils import *

# 刷新的帧率
FRAME_PER_SEC = 60

class TypeGame(object):

    def __init__(self):
        print("游戏初始化")
        #  创建游戏的窗口
        pygame.init()
        self.screen = pygame.display.set_mode((600, 500))
        self.screen.fill((255, 0, 0))
        pygame.display.set_caption('刘琦笔试')

        #  初始化参数
        self.seconds = 0
        self.clock_start = 0
        self.game_over = True
        self.clock = 0
        self.current = 0


    def gameOver(self):
        # 计时 60s
        keys = pygame.key.get_pressed()  # keys 是一个元组，穷举了所有的按键，未按下为 0，按下为 1
        if keys[K_ESCAPE]:
            sys.exit()
        # 判断时间
        if self.game_over:
            self.game_over = False
            self.clock_start = time.time()

            # 系统设置时间：60s
            self.seconds = 60
            self.clock = self.clock_start
        if not self.game_over:
            self.current = time.time() - self.clock_start
            if self.seconds < self.current:
                self.game_over = True

    def start_game(self):
        print("游戏开始...")
        # 设置初始背景值
        self.screen.fill((255, 0, 0))
        # 收集用户的输入
        type_word = TypeWord()
        show_text = showText(self.screen, type_word.massage_box)

        while True:
            # 1. 设置刷新帧率
            pygame.time.Clock().tick(FRAME_PER_SEC)
            # 监听键盘输入
            type_word.listenKey(self.screen)
            #判断是否时间是否满足
            self.gameOver()
            # 显示主提示文字
            show_text.printWord(type_word.testTexts)
            show_text.showTipe(self.game_over, type_word.score, self.seconds,self.current)
            # 更新视图
            pygame.display.update()


'''
游戏说明：
    1.打字游戏：按照给出的段落文字进行打字，空格跳到下一个单词
    2.文字提示会有延迟，按下空格后不会马上显示下一个提示单词，所以要看原文打字
    
'''

if __name__ == '__main__':

    # 创建游戏对象
    game = TypeGame()
    # 启动游戏
    game.start_game()