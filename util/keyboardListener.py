# -*- encoding: utf-8 -*-
import platform
import threading
import time
from pynput import keyboard


class KeyboardListener:
    def __init__(self, function, scanningFrequency=128):
        self.function = function  # 要执行的函数
        self.scanningFrequency = scanningFrequency  # 频率
        self.press_key_set = set()
        self.lock = threading.Lock()
        self.stop_event = threading.Event()
        self.listener_thread = None
        self.scanner_thread = None

    def on_press(self, key):
        with self.lock:
            # 记录按下的键
            try:
                if platform.system() == 'Windows':
                    t = key.vk
                else:
                    # 对于非Windows系统，使用scan属性
                    t = key.scan
            except AttributeError:
                t = key.value
                if platform.system() == 'Windows':
                    t = t.vk
                else:
                    t = t.scan
            self.press_key_set.add(int(t))

    def on_release(self, key):
        with self.lock:
            # 移除松开的键
            try:
                try:
                    if platform.system() == 'Windows':
                        t = key.vk
                    else:
                        # 对于非Windows系统，使用scan属性
                        t = key.scan
                except AttributeError:
                    t = key.value
                    if platform.system() == 'Windows':
                        t = t.vk
                    else:
                        t = t.scan
                self.press_key_set.remove(int(t))
            except KeyError:
                # 清除set
                self.press_key_set.clear()

    def start_listener(self):
        with keyboard.Listener(
                on_press=self.on_press,
                on_release=self.on_release) as listener:
            while not self.stop_event.is_set():
                time.sleep(1)  # 这里添加一个循环，以便检查停止事件

    def start_scanner(self):
        while not self.stop_event.is_set():
            time.sleep(1 / float(self.scanningFrequency))
            with self.lock:
                self.function(self.press_key_set)

    def start(self):
        self.listener_thread = threading.Thread(target=self.start_listener)
        self.scanner_thread = threading.Thread(target=self.start_scanner)

        self.listener_thread.start()
        self.scanner_thread.start()

    def stop(self):
        if not self.listener_thread is None and not self.scanner_thread is None:
            # 设置停止事件，通知监听器和扫描器线程停止
            self.stop_event.set()
            # 等待线程实际退出
            self.listener_thread.join()
            self.scanner_thread.join()
