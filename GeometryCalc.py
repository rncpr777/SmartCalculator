from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
import subprocess

Window.size = (480, 800)
Window.title = ('Geometry Calc')
Window.clearcolor = (153/255, 204/255, 255/255, 1)

class MyApp(App):
    def build(self):
        lay = FloatLayout(size=(480, 800))
        lay.add_widget(Label(text='Геометрический калькулятор',
                             font_size='30sp',
                             color=(0 / 255, 102 / 255, 204 / 255),
                             pos_hint={'y': 0.45}))
        lay.add_widget(Button(text='Площадь прямоугольника',
                              font_size='23sp',
                              size_hint=(0.65, 0.09),
                              pos_hint={'x': 0.175, 'y': 0.8},
                              background_color=(51 / 255, 255 / 255, 153 / 255),
                              color=(204 / 255, 204 / 255, 204 / 255),
                              on_press=self.runRect))
        lay.add_widget(Button(text='Площадь круга',
                              font_size='23sp',
                              size_hint=(0.65, 0.09),
                              pos_hint={'x': 0.175, 'y': 0.68},
                              background_color=(51 / 255, 255 / 255, 153 / 255),
                              color=(204 / 255, 204 / 255, 204 / 255),
                              on_press=self.runCirc))
        lay.add_widget(Button(text='Длина окружности',
                              font_size='23sp',
                              size_hint=(0.65, 0.09),
                              pos_hint={'x': 0.175, 'y': 0.56},
                              background_color=(51 / 255, 255 / 255, 153 / 255),
                              color=(204 / 255, 204 / 255, 204 / 255),
                              on_press=self.runOkr))
        lay.add_widget(Button(text='Назад',
                              font_size='34sp',
                              size_hint=(0.65, 0.09),
                              pos_hint={'x': 0.175, 'y': 0.05},
                              background_color=(51 / 255, 255 / 255, 153 / 255),
                              color=(204 / 255, 204 / 255, 204 / 255),
                              on_press=self.exit))
        return lay

    def exit(self, button):
        self.close()

    def runRect(self, button):
        subprocess.call('python Rectangle.py', shell=True)

    def runCirc(self, button):
        subprocess.call('python circle.py', shell=True)

    def runOkr(self, button):
        subprocess.call('python Okruj.py', shell=True)


if __name__ == '__main__':
    MyApp().run()