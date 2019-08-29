import os
import sys
import random
import time
import pygame
from pygame.locals import *


testTexts = "hello world"
testTxtSplit = testTexts.split()
testTxtSplitLength = len(testTxtSplit)
print(testTxtSplitLength)

pygame.init()
screen = pygame.display.set_mode((600, 500))
screen.fill((255, 0, 0))
pygame.display.set_caption('刘琦面试')
font1 = pygame.font.Font(None, 24)
font2 = pygame.font.Font(None, 30)
yellow = (255, 255, 0)

def print_text(font, x, y, text, color=(255, 255, 255)):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x, y))

correct_answer = 97
seconds = 11
score = 0
clock_start = 0
game_over = True
massage_box = []
cycleTime = 0
oldKeydowunTime = 0

while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            elif event.type == KEYDOWN:
                keydownTime = time.time()
                print(keydownTime)
                print("&"*20)
                intervalTime = keydownTime-oldKeydowunTime
                print(intervalTime)
                oldKeydowunTime = keydownTime
                if intervalTime>1:
                    intervalTime = 1
                screen.fill((255*intervalTime, 255*(1-intervalTime), 0))
                if event.key == pygame.K_SPACE:
                    print("The button is pressed")
                    print("".join(massage_box))
                    print(testTxtSplit[cycleTime])
                    if "".join(massage_box)==testTxtSplit[cycleTime]:
                        score += 1
                    massage_box.clear()
                    cycleTime += 1
                    print(cycleTime)
                else:
                    if event.key == 8:
                        massage_box.pop()
                    else:
                        massage_box.append(chr(event.key))
                        print(event.key)


        keys = pygame.key.get_pressed()     # keys 是一个元组，穷举了所有的按键，未按下为 0，按下为 1
        if keys[K_ESCAPE]:
            sys.exit()

        # 按下回车键开始
        if game_over:
            game_over = False
            clock_start = time.time()
            score = 0
            seconds = 30
            clock = clock_start

        if not game_over:
            current = time.time() - clock_start
            if seconds < current:
                game_over = True

        print_text(font1, 0, 20, "Try to keep up for 60 seconds...")
        text = "".join('%s' % ms for ms in massage_box)
        print_text(font1, 100, 450, text)

        if not game_over:
            print_text(font1, 0, 80, "Time: " + str(int(seconds-current)))

        print_text(font1, 0, 100, "the number of right word: " + str(int(score)))

        print_text(font2, 0, 240, testTexts, yellow)

        if game_over:
            os.system("pause")
            print_text(font1, 0, 160, "Press Enter to start...")

        pygame.display.update()

if __name__ == '__main__':
    pass