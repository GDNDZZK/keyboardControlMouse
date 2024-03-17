# 键盘控制鼠标

[![GitHub license](https://img.shields.io/github/license/GDNDZZK/keyboardControlMouse.svg)](https://github.com/GDNDZZK/keyboardControlMouse/blob/master/LICENSE) ![Python版本](https://img.shields.io/badge/python-3.6%2B-blue)

因为我实在找不到用着顺手的软件,于是自己写了一个。这是一个使用Python编写的程序,可以通过键盘组合键丝滑的控制鼠标,同时进行多种鼠标操作,不再需要频繁切换。

## 功能特点

- 通过简单的键盘组合键来模拟鼠标移动
- 支持模拟鼠标左键、右键和中键等基本操作,可以实现长按
- 支持模拟鼠标滚轮垂直滚动和水平滚动
- 可自定义快捷键,适应不同用户习惯
- 跨平台支持（Windows, macOS, Linux）

## 使用方法

#### 1.使用Relese版本

1. 下载并解压7z压缩包
2. 运行程序:

   ```
   keyboardControlMouse.exe
   ```
3. 开始使用键盘控制鼠标

#### 2.从源代码构建

1. 克隆或下载此仓库到本地
2. 确保你的Python版本在3.6及以上
3. 安装必要的Python库：

   ```shell
   pip install -r requirements.txt
   ```
4. 运行程序：

   ```
   app.py
   ```
5. 开始使用键盘控制鼠标

## 默认快捷键

| 功能                     | 快捷键                              | 备注                                          |
| ------------------------ | ----------------------------------- | --------------------------------------------- |
| 按住不放临时激活鼠标控制 | 「cmd(Win、Super)」+「Alt」         |                                               |
| 切换鼠标控制一直激活     | 「cmd(Win、Super)」+「Alt」+ 「/」 |                                               |
| 快速移动模式             | 「Z」                               | 激活鼠标控制后生效,可以通过设置变成"慢速模式" |
| 鼠标上移                 | 「O」                               | 激活鼠标控制后生效                            |
| 鼠标下移                 | 「L」                               | 激活鼠标控制后生效                            |
| 鼠标左移                 | 「K」                               | 激活鼠标控制后生效                            |
| 鼠标右移                 | 「;」                               | 激活鼠标控制后生效                            |
| 鼠标左键                 | 「I」                               | 激活鼠标控制后生效                            |
| 鼠标右键                 | 「P」                               | 激活鼠标控制后生效                            |
| 鼠标中键                 | 「J」                               | 激活鼠标控制后生效                            |
| 滚轮向前                 | 「U」                               | 激活鼠标控制后生效                            |
| 滚轮向后                 | 「M」                               | 激活鼠标控制后生效                            |
| 滚轮向左                 | 「,」                               | 激活鼠标控制后生效                            |
| 滚轮向右                 | 「.」                               | 激活鼠标控制后生效                            |

## 自定义设置

1. 在 `config.ini`文件中,你可以自定义你的快捷键设置。
2. 支持自定义组合键和多种触发方式,可以参考 `config.ini`中的 `ACTIVATION`
3. 需要输入按键对应的名称,如不清楚可以运行运行 `tool.exe`或在终端中运行 `tool.py`
4. 还可以调整移动速度,滚轮速度等

## 使用到的库

- [pynput](https://github.com/moses-palmer/pynput):用于获取键盘输入和控制鼠标
- [pystray](https://github.com/moses-palmer/pystray):用于创建托盘图标
- [Pillow](https://github.com/python-pillow):用于加载托盘图标的图像

## 开发者

由[GDNDZZK](https://github.com/GDNDZZK)开发和维护

## 许可证

本项目使用MIT许可证,详情请参阅[LICENSE](https://github.com/GDNDZZK/keyboardControlMouse/blob/master/LICENSE)文件
