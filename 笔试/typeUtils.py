# -*- coding: utf-8 -*-
# @Time : 2019/7/9 11:06
# @Author : 刘琦
# @FileName: typeUtils.py
# @Software: PyCharm

import os
import sys
import random
import time
import pygame
from pygame.locals import *


class TypeWord(object):
    def __init__(self):
        # 初始化原始文字
        self.text = '''an elderly carpenter was ready to retire. He told his employer contractor of his plans to leave the house building business to live a more leisurel life with his wife and enjoy his extended family. He would miss the paycheck each week,but he wanted to retire. They could get by.The contractor was sorry to see his good worker go and asked if he could build just one more house as a personal favor. The carpenter said yes,but over time it was easy to see that his heart was not materials. It was an unfortunate way to end a dedicated career.When the carpenter finished his work ,his employer came to inspect the house. Then he handed the front-door key to the carpenter and said,This is your house.'''
        self.testTexts = self.text[0:50]
        self.testTextSplit = self.testTexts.split()
        self.testTxtSplitLength = len(self.testTextSplit)

        # 初始化参数
        self.massage_box = []       #键盘输入
        self.cycleTime = 0          #循环次数
        self.oldKeydowunTime = 0    #更加键盘输入的快慢改变颜色
        self.score = 0              #最终得分
        self.paragraph = 1          #第几段
        self.oldTextSplitLength = 0 #前一段的长度
        # 切换大小写
        self.little = True
        self.flag = False

    def listenKey(self, screen):
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            elif event.type == KEYDOWN:
                keydownTime = time.time()
                intervalTime = keydownTime - self.oldKeydowunTime
                self.oldKeydowunTime = keydownTime
                if intervalTime > 1:
                    intervalTime = 1
                screen.fill((255 * intervalTime, 255 * (1 - intervalTime), 0))
                screen.blit(
                    pygame.font.Font(None, 30).render("current word hit: %s" % self.testTextSplit[self.cycleTime - self.oldTextSplitLength], True,
                                                        (0, 0, 255)),
                        (200, 200))

                # 当输入的是空格，表示一个单词输入完成
                if event.key == pygame.K_SPACE:
                    # print("The button is pressed")
                    # print("".join(self.massage_box))
                    screen.blit(
                            pygame.font.Font(None, 30).render("current word hit: %s" % self.testTextSplit[self.cycleTime - self.oldTextSplitLength], True,
                                                              (0, 0, 255)), (200, 200))
                    if "".join(self.massage_box) == self.testTextSplit[self.cycleTime - self.oldTextSplitLength]:
                        self.score += 1
                    self.massage_box.clear()
                    self.cycleTime += 1
                    if self.cycleTime == self.testTxtSplitLength*self.paragraph:
                        self.oldTextSplitLength += self.testTxtSplitLength
                        self.testTexts = self.text[0+50*self.paragraph:50+50*self.paragraph]
                        self.paragraph += 1
                        self.testTextSplit = self.testTexts.split()
                        self.testTxtSplitLength = len(self.testTextSplit)
                else:
                    # print(event.key)
                    # 判读是否切换大小写
                    if event.key == 301:
                        self.little = self.flag
                        self.flag = bool(1 - self.little)

                    # 判读是否是删除
                    # print(self.little)
                    if event.key == 8:
                        if self.massage_box:
                            self.massage_box.pop()
                    # 判读是否输入的是字母，不是则不接受
                    if 97 <= event.key <= 122 or event.key == 44 or event.key == 46:
                        if self.little:
                            self.massage_box.append(chr(event.key))
                            # print(event.key)
                        else:
                            self.massage_box.append(chr(event.key - 32))
                            # print(event.key - 32)


class showText(object):
    def __init__(self, screen, massage_box):
        self.font1 = pygame.font.Font(None, 30)
        self.font2 = pygame.font.Font(None, 35)
        self.font3 = pygame.font.Font(None, 50)
        self.yellow = (255, 255, 0)
        self.clock_start = time.time()
        self.clock = self.clock_start
        self.screen = screen
        self.massage_box = massage_box

    # 屏幕打印函数
    def print_text(self, font, x, y, text, color=(255, 255, 255)):
        imgText = font.render(text, True, color)
        self.screen.blit(imgText, (x, y))

    def printWord(self, text):
        self.print_text(self.font1, 0, 60,"*"*100)
        self.print_text(self.font1,0,80,"type as follow:")
        self.print_text(self.font1, 20, 110, text)

    # 显示提示文字
    def showTipe(self, game_over, socre, seconds, current):
        if not game_over:
            self.print_text(self.font1, 0, 200, "Time Left: " + str(int(seconds - current)))
            self.print_text(self.font1, 0, 160, "the number of right word: " + str(int(socre)))
            self.print_text(self.font1, 0, 20, "Tips:Try to keep up for 60 seconds...space to next word")
            text = "".join('%s' % ms for ms in self.massage_box)
            # 打印输入的文字
            self.print_text(self.font2, 100, 450, text)
        # 当时间结束
        if game_over:
            # 显示最终分数
            self.print_text(self.font3, 0, 250, "Final score: " + str(int(socre)))
            pygame.display.update()
            time.sleep(3)
            sys.exit()
