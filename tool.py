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
        size = get_size()
        # 通过打印一个换行符回到终端的开始
        sys.stdout.write('\r')
        # 清除到行尾的内容
        sys.stdout.write(' ' * size)
        # 再次回到行首
        sys.stdout.write(f'\r')
        sys.stdout.write('与'.join([str(t) for t in keys]))
        sys.stdout.flush()


def get_size():
    # 获取终端宽度
    size = os.get_terminal_size().columns
    # 为Windows打包后似乎只有输出80个空格才能正确覆盖上一行,我不理解这是为什么,总之先写上了
    try:
        current_file_dir = os.path.dirname(__file__)
        if '_internal' == current_file_dir[-9:]:
            size = 80
    except NameError:
        pass
    return size

def main():
    print('按键显示')
    listener = KeyboardListener(printByLine)
    listener.start()


if __name__ == '__main__':
    main()
