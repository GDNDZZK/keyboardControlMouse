#!/usr/bin/python3
# -*- encoding: utf-8 -*-
import sys
from pystray import Icon as PystrayIcon, Menu as PystrayMenu, MenuItem as PystrayMenuItem
from PIL import Image
from util.keyboardListener import KeyboardListener
from util.loadSetting import getConfigDict, keyIsPress
from util.mouseController import MouseController
mouse_ctl = MouseController()
setting_dict = getConfigDict()
left_mouse_button_flag = False
right_mouse_button_flag = False
middle_mouse_button_flag = False
mouse_scroll_up_flag = False
mouse_scroll_down_flag = False
mouse_scroll_left_flag = False
mouse_scroll_right_flag = False


def press(keys):
    """
    传入键值,判断要做的操作

    Args:
        keys:键值组成的可迭代对象
    """
    global left_mouse_button_flag, right_mouse_button_flag, middle_mouse_button_flag, mouse_scroll_up_flag, mouse_scroll_down_flag, mouse_scroll_left_flag, mouse_scroll_right_flag
    # 鼠标控制
    # 如果激活
    if keyIsPress(keys, setting_dict['ACTIVATION']):
        mouse_move_speed = float(setting_dict['MOUSE_MOVE_SPEED'])
        mouse_scroll_speed = float(setting_dict['MOUSE_SCROLL_SPEED'])
        # 判断需要执行的操作
        if keyIsPress(keys, setting_dict['MOUSE_UP']):
            print('鼠标上移')
            mouse_ctl.mouseUp(mouse_move_speed)
        if keyIsPress(keys, setting_dict['MOUSE_DOWN']):
            print('鼠标下移')
            mouse_ctl.mouseDown(mouse_move_speed)
        if keyIsPress(keys, setting_dict['MOUSE_LEFT']):
            print('鼠标左移')
            mouse_ctl.mouseLeft(mouse_move_speed)
        if keyIsPress(keys, setting_dict['MOUSE_RIGHT']):
            print('鼠标右移')
            mouse_ctl.mouseRight(mouse_move_speed)

        if not left_mouse_button_flag and keyIsPress(keys, setting_dict['LEFT_MOUSE_BUTTON']):
            left_mouse_button_flag = True
            print('鼠标左键按下')
            mouse_ctl.pressLeftButton()
        elif left_mouse_button_flag and not keyIsPress(keys, setting_dict['LEFT_MOUSE_BUTTON']):
            left_mouse_button_flag = False
            print('鼠标左键抬起')
            mouse_ctl.releaseLeftButton()
        if not right_mouse_button_flag and keyIsPress(keys, setting_dict['RIGHT_MOUSE_BUTTON']):
            right_mouse_button_flag = True
            print('鼠标右键按下')
            mouse_ctl.pressRightButton()
        elif right_mouse_button_flag and not keyIsPress(keys, setting_dict['RIGHT_MOUSE_BUTTON']):
            right_mouse_button_flag = False
            print('鼠标右键抬起')
            mouse_ctl.releaseRightButton()
        if not middle_mouse_button_flag and keyIsPress(keys, setting_dict['MIDDLE_MOUSE_BUTTON']):
            middle_mouse_button_flag = True
            print('鼠标中键按下')
            mouse_ctl.pressMiddleButton()
        elif middle_mouse_button_flag and not keyIsPress(keys, setting_dict['MIDDLE_MOUSE_BUTTON']):
            middle_mouse_button_flag = False
            print('鼠标中键抬起')
            mouse_ctl.releaseMiddleButton()

        if not mouse_scroll_up_flag and keyIsPress(keys, setting_dict['MOUSE_SCROLL_UP']):
            mouse_scroll_up_flag = True
            print('鼠标滚轮向上滚动')
            mouse_ctl.scrollUp(mouse_scroll_speed)
        elif mouse_scroll_up_flag and not keyIsPress(keys, setting_dict['MOUSE_SCROLL_UP']):
            mouse_scroll_up_flag = False
        if not mouse_scroll_down_flag and keyIsPress(keys, setting_dict['MOUSE_SCROLL_DOWN']):
            mouse_scroll_down_flag = True
            print('鼠标滚轮向下滚动')
            mouse_ctl.scrollDown(mouse_scroll_speed)
        elif mouse_scroll_down_flag and not keyIsPress(keys, setting_dict['MOUSE_SCROLL_DOWN']):
            mouse_scroll_down_flag = False
        if not mouse_scroll_left_flag and keyIsPress(keys, setting_dict['MOUSE_SCROLL_LEFT']):
            mouse_scroll_left_flag = True
            print('鼠标滚轮向左滚动')
            mouse_ctl.scrollLeft(mouse_scroll_speed)
        elif mouse_scroll_left_flag and not keyIsPress(keys, setting_dict['MOUSE_SCROLL_LEFT']):
            mouse_scroll_left_flag = False
        if not mouse_scroll_right_flag and keyIsPress(keys, setting_dict['MOUSE_SCROLL_RIGHT']):
            mouse_scroll_right_flag = True
            print('鼠标滚轮向右滚动')
            mouse_ctl.scrollRight(mouse_scroll_speed)
        elif mouse_scroll_right_flag and not keyIsPress(keys, setting_dict['MOUSE_SCROLL_RIGHT']):
            mouse_scroll_right_flag = False


def barIcon(image_path='./icon.png'):
    """
    用于显示托盘图标
    """
    global setting_dict
    def on_exit():
        print('exit触发')
        icon.stop()
    def refresh_config():
        global setting_dict
        print('refresh_config触发')
        setting_dict = getConfigDict()

    # 加载图标图像
    icon_image = Image.open(image_path)

    # 创建菜单
    menu = PystrayMenu(
        PystrayMenuItem('refreshConfig', action=refresh_config),
        PystrayMenuItem('exit', action=on_exit),
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
    listener.stop()
    sys.exit(0)


if __name__ == '__main__':
    main()
