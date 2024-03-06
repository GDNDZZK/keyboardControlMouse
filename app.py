#!/usr/bin/python3
# -*- encoding: utf-8 -*-
import os
import sys
from util.globalHotKeyManager import GlobalHotKeyManager
from util.keyboardListener import KeyboardListener
from util.loadSetting import getConfigDict, keyIsPress
from util.mouseController import MouseController
from util.SystemTrayIcon import SystemTrayIcon

left_mouse_button_flag = False
right_mouse_button_flag = False
middle_mouse_button_flag = False
mouse_scroll_up_flag = False
mouse_scroll_down_flag = False
mouse_scroll_left_flag = False
mouse_scroll_right_flag = False
permanent_activation_flag = False
permanent_activation_press_flag = False
icon_flag = False


def press(keys):
    """
    传入键值,判断要做的操作

    Args:
        keys:键值组成的可迭代对象
    """
    global sys_icon, icon_flag, permanent_activation_flag, permanent_activation_press_flag
    global left_mouse_button_flag, right_mouse_button_flag, middle_mouse_button_flag
    global mouse_scroll_up_flag, mouse_scroll_down_flag, mouse_scroll_left_flag, mouse_scroll_right_flag
    switch_permanent_activation_flag = keyIsPress(keys, setting_dict['SWITCH_PERMANENT_ACTIVATION'])
    if not permanent_activation_press_flag and switch_permanent_activation_flag:
        permanent_activation_press_flag = True
        if permanent_activation_flag:
            print('关闭一直激活')
            permanent_activation_flag = False
        else:
            print('开启一直激活')
            permanent_activation_flag = True
    elif not switch_permanent_activation_flag:
        permanent_activation_press_flag = False
    # 鼠标控制
    # 如果激活
    if permanent_activation_flag or keyIsPress(keys, setting_dict['ACTIVATION']):
        now_icon_flag = True
        mouse_move_speed = float(setting_dict['MOUSE_MOVE_SPEED'])
        mouse_move_transverse_speed = float(
            setting_dict['MOUSE_MOVE_TRANSVERSE_SPEED']) * mouse_move_speed
        mouse_move_diagonal_speed = float(
            setting_dict['MOUSE_MOVE_DIAGONAL_SPEED']) * mouse_move_speed
        mouse_scroll_speed = float(setting_dict['MOUSE_SCROLL_SPEED'])
        # 判断需要执行的操作
        mouse_up_flag = keyIsPress(keys, setting_dict['MOUSE_UP'])
        mouse_down_flag = keyIsPress(keys, setting_dict['MOUSE_DOWN'])
        mouse_left_flag = keyIsPress(keys, setting_dict['MOUSE_LEFT'])
        mouse_right_flag = keyIsPress(keys, setting_dict['MOUSE_RIGHT'])
        up_or_down_flag = mouse_up_flag or mouse_down_flag
        left_or_right_flag = mouse_left_flag or mouse_right_flag
        if mouse_up_flag:
            print('鼠标上移')
            mouse_ctl.mouseUp(
                mouse_move_diagonal_speed if left_or_right_flag else mouse_move_transverse_speed)
        if mouse_down_flag:
            print('鼠标下移')
            mouse_ctl.mouseDown(
                mouse_move_diagonal_speed if left_or_right_flag else mouse_move_transverse_speed)
        if mouse_left_flag:
            print('鼠标左移')
            mouse_ctl.mouseLeft(
                mouse_move_diagonal_speed if up_or_down_flag else mouse_move_transverse_speed)
        if mouse_right_flag:
            print('鼠标右移')
            mouse_ctl.mouseRight(
                mouse_move_diagonal_speed if up_or_down_flag else mouse_move_transverse_speed)

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
    else:
        now_icon_flag = False
    if now_icon_flag != icon_flag:
        icon_flag = now_icon_flag
        if icon_flag:
            print('点亮图标')
            sys_icon.change_icon_light()
        else:
            print('熄灭图标')
            sys_icon.change_icon_normal()


def get_paths():
    """确保工作路径正确"""
    # 获取当前工作路径
    current_work_dir = os.getcwd()
    print(f"当前工作路径：{current_work_dir}")

    # 获取当前文件所在路径
    current_file_dir = os.path.dirname(__file__)
    print(f"文件所在路径：{current_file_dir}")
    # 如果文件所在路径末尾是(_internal),跳转到上一级
    if '_internal' == current_file_dir[-9:]:
        current_file_dir = current_file_dir[:-9]
        print('internal')
        print(f"文件所在路径：{current_file_dir}")

    # 如果工作路径不是文件所在路径，切换到文件所在路径
    if current_work_dir != current_file_dir:
        os.chdir(current_file_dir)
        print("已切换到文件所在路径。")


def refresh_config():
    global setting_dict, global_hot_key
    setting_dict = getConfigDict()
    global_hot_key.delete()
    register_global_hot_key()


def register_global_hot_key():
    global global_hot_key, setting_dict
    # 遍历setting_dict
    for setting_key, setting_value in setting_dict.items():
        ext = list()
        if setting_key != 'SWITCH_PERMANENT_ACTIVATION' and setting_key != 'ACTIVATION':
            ext = setting_dict['ACTIVATION']
        for i in setting_value.split('|'):
            ext.extend(i.split('+'))
            keys = set(ext)
            global_hot_key.register(keys)


def main():
    # 确保工作路径正确
    get_paths()
    global mouse_ctl, setting_dict, sys_icon, global_hot_key
    # 鼠标控制器
    mouse_ctl = MouseController()
    # 读取设置
    setting_dict = getConfigDict()
    # 注册全局热键
    global_hot_key = GlobalHotKeyManager()
    register_global_hot_key()
    # 托盘图标
    sys_icon = SystemTrayIcon(refresh_config)
    # 开启键盘监听器
    listener = KeyboardListener(press, setting_dict['SCANNING_FREQUENCY'])
    listener.start()
    # 开启图标,阻塞主线程
    sys_icon.start()
    # 图标关闭,退出程序
    listener.stop()
    global_hot_key.delete()
    sys.exit(0)


if __name__ == '__main__':
    main()
