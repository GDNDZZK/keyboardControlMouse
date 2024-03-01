#!/usr/bin/python3
# -*- encoding: utf-8 -*-
import sys

from pystray import Icon as PystrayIcon, Menu as PystrayMenu, MenuItem as PystrayMenuItem
from PIL import Image, ImageDraw
from util.keyboardListener import KeyboardListener
from util.loadSetting import getConfigDict, keyIsPress
setting_dict = getConfigDict()

left_mouse_button_flag = False
right_mouse_button_flag = False
middle_mouse_button_flag = False
mouse_scroll_up_flag = False
mouse_scroll_down_flag = False


def press(keys):
    """
    传入键值,判断要做的操作

    Args:
        keys:键值组成的可迭代对象
    """
    global left_mouse_button_flag, right_mouse_button_flag, middle_mouse_button_flag,mouse_scroll_up_flag,mouse_scroll_down_flag
    # TODO 鼠标控制
    # 如果激活
    if keyIsPress(keys, setting_dict['ACTIVATION']):
        # 判断需要执行的操作
        if keyIsPress(keys, setting_dict['MOUSE_UP']):
            print('鼠标上移')
        if keyIsPress(keys, setting_dict['MOUSE_DOWN']):
            print('鼠标下移')
        if keyIsPress(keys, setting_dict['MOUSE_LEFT']):
            print('鼠标左移')
        if keyIsPress(keys, setting_dict['MOUSE_RIGHT']):
            print('鼠标右移')

        if not left_mouse_button_flag and keyIsPress(keys, setting_dict['LEFT_MOUSE_BUTTON']):
            left_mouse_button_flag = True
            print('鼠标左键按下')
        elif left_mouse_button_flag and not keyIsPress(keys, setting_dict['LEFT_MOUSE_BUTTON']):
            left_mouse_button_flag = False
            print('鼠标左键抬起')
        if not right_mouse_button_flag and keyIsPress(keys, setting_dict['RIGHT_MOUSE_BUTTON']):
            right_mouse_button_flag = True
            print('鼠标右键按下')
        elif right_mouse_button_flag and not keyIsPress(keys, setting_dict['RIGHT_MOUSE_BUTTON']):
            right_mouse_button_flag = False
            print('鼠标右键抬起')
        if not middle_mouse_button_flag and keyIsPress(keys, setting_dict['MIDDLE_MOUSE_BUTTON']):
            middle_mouse_button_flag = True
            print('鼠标中键按下')
        elif middle_mouse_button_flag and not keyIsPress(keys, setting_dict['MIDDLE_MOUSE_BUTTON']):
            middle_mouse_button_flag = False
            print('鼠标中键抬起')

        if not mouse_scroll_up_flag and keyIsPress(keys, setting_dict['MOUSE_SCROLL_UP']):
            mouse_scroll_up_flag = True
            print('鼠标滚轮向上滚动')
        elif mouse_scroll_up_flag and not keyIsPress(keys, setting_dict['MOUSE_SCROLL_UP']):
            mouse_scroll_up_flag = False
        if not mouse_scroll_down_flag and keyIsPress(keys, setting_dict['MOUSE_SCROLL_DOWN']):
            mouse_scroll_down_flag = True
            print('鼠标滚轮向下滚动')
        elif mouse_scroll_down_flag and not keyIsPress(keys, setting_dict['MOUSE_SCROLL_DOWN']):
            mouse_scroll_down_flag = False
        if keyIsPress(keys, setting_dict['MOUSE_SCROLL_UP_QUICK']):
            print('鼠标滚轮向上滚动')
        if keyIsPress(keys, setting_dict['MOUSE_SCROLL_DOWN_QUICK']):
            print('鼠标滚轮向下滚动')


def barIcon(image_path='./icon.png'):
    """
    用于显示托盘图标
    """
    def on_exit():
        print('exit触发')
        icon.stop()

    # 加载图标图像
    icon_image = Image.open(image_path)

    # 创建菜单
    menu = PystrayMenu(
        PystrayMenuItem('exit', action=on_exit)
    )

    # 创建图标
    icon = PystrayIcon('keyboardOperatedMouse', icon_image,
                       'keyboardOperatedMouse', menu)

    # 开始运行图标
    icon.run()


def main():
    # 开启键盘监听器
    listener = KeyboardListener(press, setting_dict['SCANNING_FREQUENCY'])
    listener.start()
    # 开启图标,阻塞主线程
    barIcon()
    # 图标关闭,退出程序
    exit(0)


if __name__ == '__main__':
    main()
