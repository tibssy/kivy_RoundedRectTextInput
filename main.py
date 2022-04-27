from kivymd.app import MDApp
# from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder


Builder.load_file('layout.kv')


class MyLayout(BoxLayout):
    pass


class DemoApp(MDApp):
# class DVRApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    DemoApp().run()
