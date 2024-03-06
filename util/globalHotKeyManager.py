from pynput import keyboard
import warnings
import logging


class GlobalHotKeyManager:
    """一利用GlobalHotKeys注册全局快捷键,提供注册函数和删除函数"""

    def __init__(self):
        self.hotkeys = {}  # 一个字典，存储已注册的全局快捷键和对应的回调函数
        self.global_hotkeys = None  # 一个GlobalHotKeys对象，用于监听键盘事件

    def register(self, keys, callback=None):
        """注册函数,传入包含int类型键值的set,将set包含的按键组合注册为全局快捷键,传入回调函数,当按键组合被触发时执行,如果不传入回调函数,使用默认的回调函数"""
        # TODO 将键值set转换为字符串表示，例如{17, 18, 72}转换为'<ctrl>+<alt>+h'
        keys_str = '+'.join(f'<{keyboard.key_to_name(key)}>' for key in keys)
        # 如果没有传入回调函数，使用默认的回调函数
        if callback is None:
            callback = self.default_callback(keys_str)
        # 尝试将按键组合和回调函数添加到字典中
        try:
            self.hotkeys[keys_str] = callback
        except ValueError as e:
            # 如果出现ValueError异常，说明这个快捷键已经被占用，发出一个警告信息，并记录异常信息
            warnings.warn(f'{keys_str} is already registered by another program.')
            logging.exception(e)
            return
        # 如果已经有GlobalHotKeys对象，先停止它
        if self.global_hotkeys:
            self.global_hotkeys.stop()
        # 尝试创建一个新的GlobalHotKeys对象，传入字典
        try:
            self.global_hotkeys = keyboard.GlobalHotKeys(self.hotkeys)
        except ValueError as e:
            # 如果出现ValueError异常，说明有些快捷键已经被占用，发出一个警告信息，并记录异常信息
            warnings.warn('Some hotkeys are already registered by another program.')
            logging.exception(e)
            return
        # 启动GlobalHotKeys对象，开始监听键盘事件
        self.global_hotkeys.start()

    def delete(self):
        """删除函数,用于删除所有通过注册函数注册的全局快捷键"""
        # 如果有GlobalHotKeys对象，停止它
        if self.global_hotkeys:
            self.global_hotkeys.stop()
        # 清空字典
        self.hotkeys.clear()
        # 将GlobalHotKeys对象设为None
        self.global_hotkeys = None

    def default_callback(self, keys_str):
        """默认的回调函数,作用是在终端中输出一条info,表示被按下的快捷键"""
        def inner():
            print(f'{keys_str} pressed')
        return inner
