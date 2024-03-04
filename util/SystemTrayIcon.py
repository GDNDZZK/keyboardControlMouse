from pystray import Icon as PystrayIcon, Menu as PystrayMenu, MenuItem as PystrayMenuItem
from PIL import Image


class SystemTrayIcon:
    def __init__(self, refresh_config_def, image_path='./icon.png', light_image_path='./icon_light.png'):
        self.icon_image = Image.open(image_path)
        self.light_icon_image = Image.open(light_image_path)
        self.refresh_config_def = refresh_config_def
        self.menu = PystrayMenu(
            PystrayMenuItem('refreshConfig', action=self.refresh_config),
            PystrayMenuItem('exit', action=self.on_exit),
        )

    def start(self):
        self.icon = PystrayIcon('keyboardControlMouse', self.icon_image,
                                'keyboardControlMouse', self.menu)
        self.icon.run()

    def on_exit(self):
        print('exit触发')
        self.icon.stop()

    def change_icon(self, image):
        """
        改变任务栏图标
        """
        self.icon.icon = image

    def refresh_config(self):
        print('refresh_config触发')
        self.refresh_config_def

    def change_icon_light(self):
        """
        切换任务栏图标
        """
        self.change_icon(self.light_icon_image)

    def change_icon_normal(self):
        """
        切换任务栏图标
        """
        self.change_icon(self.icon_image)
