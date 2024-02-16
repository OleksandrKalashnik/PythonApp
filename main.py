from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class StartApp(MDApp):
    def build(self):
        return MDLabel(text="Hello, StartApp", halign="center")


StartApp().run()