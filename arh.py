from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

Window.size = (480, 800)
Window.title = ('Trenie')
Window.clearcolor = (153/255, 204/255, 255/255, 1)

class MyApp(App):
    def __init__(self):
        super().__init__()
        self.inp1 = TextInput(text='Плотность жидкости',
                              size_hint=(0.8, 0.08),
                              pos_hint={'y': 0.77, 'x': 0.1},
                              font_size='34sp',
                              multiline=False)

        self.inp2 = TextInput(text='Объём погруженной части',
                              size_hint=(0.8, 0.08),
                              pos_hint={'y': 0.67, 'x': 0.1},
                              font_size='30sp',
                              multiline=False)

        self.outp = TextInput(text='Сила Архимеда',
                              size_hint=(0.8, 0.08),
                              pos_hint={'y': 0.48, 'x': 0.1},
                              font_size='34sp',
                              multiline=False,
                              readonly=True)

    def build(self):
        lay = FloatLayout(size=(480, 800))
        lay.add_widget(Label(text='Сила Архимеда',
                             font_size='45sp',
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
        lay.add_widget(self.inp2)
        lay.add_widget(self.outp)
        return lay

    def count(self, button):
        m = self.inp1.text
        u = self.inp2.text
        try:
            m = float(m)
            u = float(u)
        except:
            self.outp.text = ('!!!Вводите число!!!')
            return None
        res = u * m * 9.8
        res = round(res, 3)
        res = str(res) + ' H'
        self.outp.text = res

    def back(self, button):
        MyApp().close()


if __name__ == '__main__':
    MyApp().run()