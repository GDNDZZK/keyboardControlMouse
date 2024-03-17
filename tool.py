#!/usr/bin/python3
# -*- encoding: utf-8 -*-
import sys
import os
from util.keyboardListener import KeyboardListener

keys_record = set()
def printByLine(keys):
    global keys_record
    if not set(keys) == keys_record:
        keys_record = set(keys)
        # 获取终端宽度
        size = os.get_terminal_size().columns
        # 通过打印一个换行符回到终端的开始
        sys.stdout.write('\r')
        # 清除到行尾的内容
        sys.stdout.write(' ' * size)
        # 再次回到行首
        sys.stdout.write('\r')
        sys.stdout.write('与'.join([str(t) for t in keys]))
        sys.stdout.flush()


def main():
    print('按键显示')
    listener = KeyboardListener(printByLine)
    listener.start()


if __name__ == '__main__':
    main()
