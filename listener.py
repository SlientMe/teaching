import sys, os
import random
import time
import pygame
from pygame.locals import *
from pynput.keyboard import Controller, Key, Listener

# 监听按压ahello world ahello worldahello worldahello world ahello world
# def on_press(key):
#     print(key)
#     if key == "Key.space":
#         print("执行了if阿")
#     try:
#         print("正在按压:", format(key.char))
#     except AttributeError:
#         print("在按压:", format(key))

# 监听释放ahello world ahello world

def on_release(key):
    print("已经释放:", format(key))
    if format(key) == "Key.space":
        print("执行了if阿")
    if key == Key.esc:
        # 停止监听
        return False

# 开始监听
def start_listen():
    with Listener(on_release=on_release) as listener:
        listener.join()

#pygame开始ahello world
pygame.init()


if __name__ == '__main__':
    # 实例化键盘
    kb = Controller()
    # 使用键盘输入一个字母
    # kb.press('a')
    # kb.release('a')
    # # 使用键盘输入字符串,注意当前键盘调成英文
    # kb.type("hello world")
    # # 使用Key.xxx输入
    # kb.press(Key.space)

    # 开始监听,按esc退出监听
    start_listen()
