from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

Window.size = (480, 800)
Window.title = ('Kvadr Urav')
Window.clearcolor = (153/255, 204/255, 255/255, 1)

class MyApp(App):
    def __init__(self):
        super().__init__()
        self.inp1 = TextInput(text='',
                              size_hint=(0.08, 0.08),
                              pos_hint={'x': 0.08, 'y': 0.66},
                              font_size='15sp',
                              multiline=False)
        self.inp2 = TextInput(text='',
                              size_hint=(0.08, 0.08),
                              pos_hint={'x': 0.43, 'y': 0.66},
                              font_size='15sp',
                              multiline=False)
        self.inp3 = TextInput(text='',
                              size_hint=(0.08, 0.08),
                              pos_hint={'x': 0.75, 'y': 0.66},
                              font_size='15sp',
                              multiline=False)
        self.out1 = TextInput(text='                 X1',
                              size_hint=(0.6, 0.08),
                              pos_hint={'x': 0.2, 'y': 0.5},
                              font_size='27sp',
                              multiline=False,
                              readonly=True)
        self.out2 = TextInput(text='                 X2',
                              size_hint=(0.6, 0.08),
                              pos_hint={'x': 0.2, 'y': 0.37},
                              font_size='27sp',
                              multiline=False,
                              readonly=True)

    def build(self):
        lay = FloatLayout(size=(480, 800))
        lay.add_widget(Label(text='Квадратные уравнения',
                             font_size='37sp',
                             color=(0 / 255, 102 / 255, 204 / 255),
                             pos_hint={'y': 0.43}))
        lay.add_widget(Label(text='X^2   +',
                             font_size='37sp',
                             color=(0 / 255, 0 / 255, 0 / 255),
                             pos_hint={'x': -0.22, 'y': 0.2}))
        lay.add_widget(Label(text='X   +',
                             font_size='37sp',
                             color=(0 / 255, 0 / 255, 0 / 255),
                             pos_hint={'x': 0.1, 'y': 0.2}))
        lay.add_widget(Label(text=' =  0',
                             font_size='37sp',
                             color=(0 / 255, 0 / 255, 0 / 255),
                             pos_hint={'x': 0.4, 'y': 0.2}))
        lay.add_widget(Button(text='Посчитать',
                              font_size='30sp',
                              size_hint=(0.65, 0.09),
                              pos_hint={'x': 0.175, 'y': 0.17},
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
        lay.add_widget(self.inp3)
        lay.add_widget(self.out1)
        lay.add_widget(self.out2)
        return lay

    def count(self, button):
        a = self.inp1.text
        b = self.inp2.text
        c = self.inp3.text
        try:
            a = float(a)
            b = float(b)
            c = float(c)
        except:
            self.out1.text = '   !!!Вводите числа!!!'
            self.out2.text = '   !!!Вводите числа!!!'
            return None
        d = b * b
        d = d - 4 * a * c
        if d < 0:
            self.out1.text = '!!!Отрицательный D!!!'
            self.out2.text = '!!!Отрицательный D!!!'
            return None
        d = d ** 0.5
        x1 = -b + d
        x1 = x1 / 2
        x1 = str(round(x1, 3))
        x2 = -b - d
        x2 = x2 / 2
        x2 = str(round(x2, 3))
        self.out1.text = x1
        self.out2.text = x2

    def back(self, button):
        MyApp().close()


if __name__ == '__main__':
    MyApp().run()