from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
import subprocess

Window.size = (480, 800)
Window.title = ('Smart Calc')
Window.clearcolor = (153/255, 204/255, 255/255, 1)

class MyApp(App):
    def build(self):
        lay = FloatLayout(size=(480, 800))
        lay.add_widget(Label(text='Умный калькулятор',
                             font_size='40sp',
                             color=(0/255, 102/255, 204/255),
                             pos_hint={'y': 0.45}))
        lay.add_widget(Button(text='Простой калькулятор',
                              font_size='20sp',
                              size_hint=(0.65, 0.09),
                              pos_hint={'x': 0.175, 'y': 0.8},
                              background_color=(51/255, 255/255, 153/255),
                              color=(204/255, 204/255, 204/255),
                              on_press=self.launchSC))
        lay.add_widget(Button(text='Физический калькулятор',
                              font_size='20sp',
                              size_hint=(0.65, 0.09),
                              pos_hint={'x': 0.175, 'y': 0.68},
                              background_color=(51/255, 255/255, 153/255),
                              color=(204/255, 204/255, 204/255),
                              on_press=self.launchPC))
        lay.add_widget(Button(text='Геометрический калькулятор',
                              font_size='20sp',
                              size_hint=(0.65, 0.09),
                              pos_hint={'x': 0.175, 'y': 0.56},
                              background_color=(51 / 255, 255 / 255, 153 / 255),
                              color=(204 / 255, 204 / 255, 204 / 255),
                              on_press=self.launchGC))
        lay.add_widget(Button(text='Квадратные уравнения',
                              font_size='20sp',
                              size_hint=(0.65, 0.09),
                              pos_hint={'x': 0.175, 'y': 0.44},
                              background_color=(51 / 255, 255 / 255, 153 / 255),
                              color=(204 / 255, 204 / 255, 204 / 255),
                              on_press=self.launchKU))
        lay.add_widget(Button(text='Выйти',
                              font_size='20sp',
                              size_hint=(0.65, 0.09),
                              pos_hint={'x': 0.175, 'y': 0.05},
                              background_color=(51 / 255, 255 / 255, 153 / 255),
                              color=(204 / 255, 204 / 255, 204 / 255),
                              on_press=self.exit))
        return lay

    def launchSC(self, button):
        subprocess.call('python SimpleCalc.py', shell=True)

    def launchPC(self, button):
        subprocess.call('python PhysicalCalc.py', shell=True)

    def launchGC(self, button):
        subprocess.call('python GeometryCalc.py', shell=True)

    def launchKU(self, button):
        subprocess.call('python KvadrUr.py', shell=True)

    def exit(self, button):
        self.close()


if __name__ == '__main__':
    MyApp().run()