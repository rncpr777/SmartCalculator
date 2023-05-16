from kivy.app import App
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

Window.size = (480, 800)
Window.clearcolor = (153/255, 204/255, 255/255, 1)

class MyApp(App):
    def __init__(self):
        super().__init__()
        self.in1 = TextInput(text='Первое число',
                             size_hint=(0.45, 0.1),
                             pos_hint={'y': 0.8, 'x': 0.025},
                             font_size='27sp',
                             background_color=(240/255, 240/255, 240/255),
                             multiline=False)
        self.in2 = TextInput(text='Второе число',
                             size_hint=(0.45, 0.1),
                             pos_hint={'y': 0.8, 'x': 0.525},
                             font_size='27sp',
                             background_color=(240 / 255, 240 / 255, 240 / 255),
                             multiline=False)
        self.in3 = TextInput(text='*результат*',
                             size_hint=(0.9, 0.1),
                             readonly=True,
                             pos_hint={'x': 0.05, 'y': 0.17},
                             multiline=False,
                             background_color=(240 / 255, 240 / 255, 240 / 255),
                             font_size='45sp')

    def build(self):
        lay = FloatLayout(size=(480, 800))
        lay.add_widget(Label(text='Простой калькулятор',
                             font_size='40sp',
                             color=(0/255, 102/255, 204/255),
                             pos_hint={'y': 0.45}))
        lay.add_widget(self.in1)
        lay.add_widget(self.in2)
        lay.add_widget(Button(text='+',
                              size_hint=(0.4, 0.12),
                              pos_hint={'y': 0.57, 'x': 0.05},
                              font_size='45sp',
                              background_color=(51 / 255, 255 / 255, 153 / 255),
                              color=(204 / 255, 204 / 255, 204 / 255),
                              on_press=self.plussed))
        lay.add_widget(Button(text='-',
                              size_hint=(0.4, 0.12),
                              pos_hint={'y': 0.57, 'x': 0.55},
                              font_size='45sp',
                              background_color=(51 / 255, 255 / 255, 153 / 255),
                              color=(204 / 255, 204 / 255, 204 / 255),
                              on_press=self.minused))
        lay.add_widget(Button(text='X',
                              size_hint=(0.4, 0.12),
                              pos_hint={'y': 0.37, 'x': 0.05},
                              font_size='45sp',
                              background_color=(51 / 255, 255 / 255, 153 / 255),
                              color=(204 / 255, 204 / 255, 204 / 255),
                              on_press=self.multied))
        lay.add_widget(Button(text='0|0',
                              size_hint=(0.4, 0.12),
                              pos_hint={'y': 0.37, 'x': 0.55},
                              font_size='45sp',
                              background_color=(51 / 255, 255 / 255, 153 / 255),
                              color=(204 / 255, 204 / 255, 204 / 255),
                              on_press=self.halfed))
        lay.add_widget(self.in3)
        lay.add_widget(Button(text='Назад',
                              font_size='30sp',
                              size_hint=(0.65, 0.09),
                              pos_hint={'x': 0.175, 'y': 0.03},
                              background_color=(51 / 255, 255 / 255, 153 / 255),
                              color=(204 / 255, 204 / 255, 204 / 255),
                              on_press=self.back))
        return lay

    def plussed(self, button):
        tt = self.in1.text
        tt1 = self.in2.text
        try:
            tt = float(tt)
            tt1 = float(tt)
        except:
            self.in3.text = '!!!Вводите число!!!'
            return
        self.in3.text = str(round(float(self.in1.text) + float(self.in2.text), 3))
    def minused(self, button):
        tt = self.in1.text
        tt1 = self.in2.text
        try:
            tt = float(tt)
            tt1 = float(tt1)
        except:
            self.in3.text = '!!!Вводите число!!!'
            return
        self.in3.text = str(round(float(self.in1.text) - int(self.in2.text), 3))
    def multied(self, button):
        tt = self.in1.text
        tt1 = self.in2.text
        try:
            tt = float(tt)
            tt1 = float(tt1)
        except:
            self.in3.text = '!!!Вводите число!!!'
            return
        self.in3.text = str(round(float(self.in1.text) * float(self.in2.text), 3))
    def halfed(self, button):
        tt = self.in1.text
        tt1 = self.in2.text
        try:
            tt = float(tt)
            tt1 = float(tt1)
        except:
            self.in3.text = '!!!Вводите число!!!'
            return
        if self.in2.text == '0' or self.in2.text == 0:
            self.in3.text = 'Ошибка...'
        else:
            self.in3.text = str(round(float(self.in1.text) / float(self.in2.text), 3))

    def back(self, button):
        MyApp().close()


if __name__ == '__main__':
    MyApp().run()