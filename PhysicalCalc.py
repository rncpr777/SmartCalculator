from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
import subprocess

Window.size = (480, 800)
Window.title = ('Physical Calc')
Window.clearcolor = (153/255, 204/255, 255/255, 1)

class MyApp(App):
    def build(self):
        lay = FloatLayout(size=(480, 800))
        lay.add_widget(Label(text='Физический калькулятор',
                             font_size='35sp',
                             color=(0 / 255, 102 / 255, 204 / 255),
                             pos_hint={'y': 0.45}))
        lay.add_widget(Button(text='Сила тяжести у поверхности',
                              font_size='20sp',
                              size_hint=(0.65, 0.09),
                              pos_hint={'x': 0.175, 'y': 0.8},
                              background_color=(51 / 255, 255 / 255, 153 / 255),
                              color=(204 / 255, 204 / 255, 204 / 255),
                              on_press=self.launchfindg))
        lay.add_widget(Button(text='Сила трения',
                              font_size='20sp',
                              size_hint=(0.65, 0.09),
                              pos_hint={'x': 0.175, 'y': 0.67},
                              background_color=(51 / 255, 255 / 255, 153 / 255),
                              color=(204 / 255, 204 / 255, 204 / 255),
                              on_press=self.trenie))
        lay.add_widget(Button(text='Сила упругости',
                              font_size='20sp',
                              size_hint=(0.65, 0.09),
                              pos_hint={'x': 0.175, 'y': 0.54},
                              background_color=(51 / 255, 255 / 255, 153 / 255),
                              color=(204 / 255, 204 / 255, 204 / 255),
                              on_press=self.uprug))
        lay.add_widget(Button(text='Сила Архимеда',
                              font_size='20sp',
                              size_hint=(0.65, 0.09),
                              pos_hint={'x': 0.175, 'y': 0.42},
                              background_color=(51 / 255, 255 / 255, 153 / 255),
                              color=(204 / 255, 204 / 255, 204 / 255),
                              on_press=self.arh))
        lay.add_widget(Button(text='Назад',
                              font_size='30sp',
                              size_hint=(0.65, 0.09),
                              pos_hint={'x': 0.175, 'y': 0.05},
                              background_color=(51 / 255, 255 / 255, 153 / 255),
                              color=(204 / 255, 204 / 255, 204 / 255),
                              on_press=self.back))
        return lay

    def launchfindg(self, button):
        subprocess.call('python Findg.py', shell=True)

    def trenie(self, button):
        subprocess.call('python Trenie.py', shell=True)

    def uprug(self, button):
        subprocess.call('python uprug.py', shell=True)

    def arh(self, button):
        subprocess.call('python arh.py', shell=True)

    def back(self, button):
        MyApp().close()


if __name__ == '__main__':
    MyApp().run()