from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import math

Window.size = (480, 800)
Window.title = ('Find okr')
Window.clearcolor = (153/255, 204/255, 255/255, 1)

class MyApp(App):
    def __init__(self):
        super().__init__()
        self.inp1 = TextInput(text='Радиус',
                              size_hint=(0.8, 0.08),
                              pos_hint={'y': 0.7, 'x': 0.1},
                              font_size='34sp',
                              multiline=False)
        self.out = TextInput(text='*Длина окружности*',
                             size_hint=(0.8, 0.08),
                             pos_hint={'y': 0.4, 'x': 0.1},
                             font_size='25sp',
                             multiline=False,
                             readonly=True)

    def build(self):
        lay = FloatLayout(size=(480, 800))
        lay.add_widget(Label(text='Длина окружности',
                             font_size='37sp',
                             color=(0 / 255, 102 / 255, 204 / 255),
                             pos_hint={'y': 0.43}))
        lay.add_widget(Button(text='Рассчитать',
                              font_size='30sp',
                              size_hint=(0.65, 0.09),
                              pos_hint={'x': 0.175, 'y': 0.18},
                              background_color=(51 / 255, 255 / 255, 153 / 255),
                              color=(204 / 255, 204 / 255, 204 / 255),
                              on_press=self.count))
        lay.add_widget(Button(text='Назад',
                              font_size='30sp',
                              size_hint=(0.65, 0.09),
                              pos_hint={'x': 0.175, 'y': 0.05},
                              background_color=(51 / 255, 255 / 255, 153 / 255),
                              color=(204 / 255, 204 / 255, 204 / 255),
                              on_press=self.back))
        lay.add_widget(self.inp1)
        lay.add_widget(self.out)
        return lay

    def count(self, button):
        r = self.inp1.text
        try:
            r = float(r)
        except:
            self.out.text = '!!!Вводите числа!!!'
            return None
        c = 2 * math.pi * r
        c = str(round(c, 3))
        self.out.text = c

    def back(self, button):
        MyApp().close()


if __name__ == '__main__':
    MyApp().run()