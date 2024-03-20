# keyboardControlMouse

[![GitHub license](https://img.shields.io/github/license/GDNDZZK/keyboardControlMouse.svg)](https://github.com/GDNDZZK/keyboardControlMouse/blob/master/LICENSE) ![Python版本](https://img.shields.io/badge/python-3.6%2B-blue)
I wrote this program because I couldn't find a software I was satisfied with. It is a program written in Python that can smoothly control the mouse through keyboard combinations, supporting multiple mouse operations without the need to switch frequently.
[Demo Video](https://www.bilibili.com/video/BV1xH4y1s7kg)

[中文](./README.zh.md)

## Features

- Control mouse movement through simple keyboard shortcuts
- Support mouse left/right/middle button operations, including long press
- Support mouse scroll wheel vertical/horizontal scrolling
- Customizable shortcuts to suit different user habits
- Cross-platform support (Windows, macOS, Linux)

## Usage

### Using the Release Version

1. Download and extract the 7z archive
2. Run the program:

   ```
   keyboardControlMouse.exe
   ```
3. Start using the keyboard to control the mouse

### Building from Source

1. Clone or download this repository to your local machine
2. Ensure your Python version is 3.6 or above
3. Install the necessary Python libraries:

   ```
   pip install -r requirements.txt
   ```
4. Run the program:

   ```
   app.py
   ```
5. Start using the keyboard to control the mouse

## Default Shortcuts

| Function                           | Shortcut                        | Notes                                                                    |
| ---------------------------------- | ------------------------------- | ------------------------------------------------------------------------ |
| Temporarily activate mouse control | 'cmd(Win、Super)' + 'Alt'       |                                                                          |
| Toggle mouse control on/off        | 'cmd(Win、Super)' + 'Alt' + '/' |                                                                          |
| Fast move mode                     | 'Z'                             | Effective after activating mouse control, can be switched to "slow mode" |
| Move mouse up                      | 'O'                             | Effective after activating mouse control                                 |
| Move mouse down                    | 'L'                             | Effective after activating mouse control                                 |
| Move mouse left                    | 'K'                             | Effective after activating mouse control                                 |
| Move mouse right                   | ';'                             | Effective after activating mouse control                                 |
| Mouse left button                  | 'I'                             | Effective after activating mouse control                                 |
| Mouse right button                 | 'P'                             | Effective after activating mouse control                                 |
| Mouse middle button                | 'J'                             | Effective after activating mouse control                                 |
| Scroll wheel up                    | 'U'                             | Effective after activating mouse control                                 |
| Scroll wheel down                  | 'M'                             | Effective after activating mouse control                                 |
| Scroll wheel left                  | ','                             | Effective after activating mouse control                                 |
| Scroll wheel right                 | '.'                             | Effective after activating mouse control                                 |

## Custom Settings

1. You can customize your shortcut settings in the `config.ini` file.
2. Support custom key combinations and multiple trigger methods, refer to `ACTIVATION` in `config.ini`.
3. You need to enter the key name. If you are unsure of the key name, you can run `tool.exe` or `tool.py` in the terminal.
4. You can also adjust the move speed, scroll speed, etc.

## Used Libraries

- [pynput](https://github.com/moses-palmer/pynput): For capturing keyboard input and controlling mouse
- [pystray](https://github.com/moses-palmer/pystray): For creating tray icons
- [Pillow](https://github.com/python-pillow): For loading images for tray icons

## Developer

Developed and maintained by [GDNDZZK](https://github.com/GDNDZZK)

## License

This project is licensed under the MIT License, see the [LICENSE](https://github.com/GDNDZZK/keyboardControlMouse/blob/master/LICENSE) file for details
