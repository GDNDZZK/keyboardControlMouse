# -*- encoding: utf-8 -*-
from pynput.mouse import Button, Controller


class MouseController:
    """鼠标控制类，包含鼠标的常用操作方法"""

    def __init__(self):
        """初始化鼠标控制器"""
        self.mouse = Controller()

    def getPosition(self):
        """
        获取鼠标指针的当前坐标

        Returns:
        - x,y
        """
        return self.mouse.position

    def setPosition(self, x, y):
        """
        设置鼠标指针的坐标位置

        Args:
        - x: 横坐标
        - y: 纵坐标
        """
        self.mouse.position = (x, y)

    def mouseUp(self, mouse_move_speed=1):
        """鼠标向上移动"""
        x, y = self.getPosition()
        self.setPosition(x, y-mouse_move_speed)

    def mouseDown(self, mouse_move_speed=1):
        """鼠标向下移动"""
        x, y = self.getPosition()
        self.setPosition(x, y+mouse_move_speed)

    def mouseLeft(self, mouse_move_speed=1):
        """鼠标向左移动"""
        x, y = self.getPosition()
        self.setPosition(x-mouse_move_speed, y)

    def mouseRight(self, mouse_move_speed=1):
        """鼠标向右移动"""
        x, y = self.getPosition()
        self.setPosition(x+mouse_move_speed, y)

    def pressLeftButton(self):
        """鼠标左键按下"""
        self.mouse.press(Button.left)

    def releaseLeftButton(self):
        """鼠标左键抬起"""
        self.mouse.release(Button.left)

    def pressRightButton(self):
        """鼠标右键按下"""
        self.mouse.press(Button.right)

    def releaseRightButton(self):
        """鼠标右键抬起"""
        self.mouse.release(Button.right)

    def pressMiddleButton(self):
        """鼠标中键按下"""
        self.mouse.press(Button.middle)

    def releaseMiddleButton(self):
        """鼠标中键抬起"""
        self.mouse.release(Button.middle)

    def scrollUp(self, mouse_scroll_speed=3):
        """鼠标滚轮向上滚动"""
        self.mouse.scroll(0, mouse_scroll_speed)

    def scrollDown(self, mouse_scroll_speed=3):
        """鼠标滚轮向下滚动"""
        self.mouse.scroll(0, -1 * mouse_scroll_speed)

    def scrollLeft(self, mouse_scroll_speed=3):
        """鼠标滚轮向左滚动"""
        self.mouse.scroll(-1 * mouse_scroll_speed, 0)

    def scrollRight(self, mouse_scroll_speed=3):
        """鼠标滚轮向右滚动"""
        self.mouse.scroll(mouse_scroll_speed, 0)
