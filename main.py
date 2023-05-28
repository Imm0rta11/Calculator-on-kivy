from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
from kivy.uix.label import Label
from operator import add, sub, mul, truediv

x = None
y = None
A = None

Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 400)
Config.set('graphics', 'height', 600)
bnt_text = None

label = None
label1 = None
class CalculatorApp(App):
    def equel(self):
        global A
        global x
        global y
        try:
            expression = label.text
            if '+' in expression:
                x, y = expression.split('+')
                A = str(add(float(x), float(y)))
                self.update_label(str(A))
            if '-' in expression:
                x, y = expression.split('-')
                A = str(sub(float(x), float(y)))
                self.update_label(str(A))
            if '*' in expression:
                x, y = expression.split('*')
                A = str(mul(float(x), float(y)))
                self.update_label(str(A))
            if '/' in expression:
                x, y = expression.split('/')
                A = str(truediv(float(x), float(y)))
                self.update_label(str(A))
        except ValueError:
            self.update_label('Error')
        except ZeroDivisionError:
            self.update_label('Error')
    def clear(self):
        self.update_label('0')

    def update_label(self, text):
        label.text = text

    def add_digit(self, bnt_text: str) -> None:
        if label.text == '0':
            self.update_label(bnt_text)
        else:
            self.update_label(label.text + bnt_text)

    def build(self):
        global label
        global label1
        bl = BoxLayout(orientation='vertical', padding=25)
        gl = GridLayout(cols=4, spacing=3)

        label = Label(text='0', font_size=90)
        bl.add_widget(label)

        gl.add_widget(Button(text='C', on_press=lambda instance: self.clear()))
        gl.add_widget(Button(text='', on_press=lambda instance: self.add_digit('')))
        gl.add_widget(Button(text='', on_press=lambda instance: self.add_digit('')))
        gl.add_widget(Button(text='/', on_press=lambda instance: self.add_digit('/')))

        gl.add_widget(Button(text='7', on_press=lambda instance: self.add_digit('7')))
        gl.add_widget(Button(text='8', on_press=lambda instance: self.add_digit('8')))
        gl.add_widget(Button(text='9', on_press=lambda instance: self.add_digit('9')))
        gl.add_widget(Button(text='*', on_press=lambda instance: self.add_digit('*')))

        gl.add_widget(Button(text='4', on_press=lambda instance: self.add_digit('4')))
        gl.add_widget(Button(text='5', on_press=lambda instance: self.add_digit('5')))
        gl.add_widget(Button(text='6', on_press=lambda instance: self.add_digit('6')))
        gl.add_widget(Button(text='-', on_press=lambda instance: self.add_digit('-')))

        gl.add_widget(Button(text='1', on_press=lambda instance: self.add_digit('1')))
        gl.add_widget(Button(text='2', on_press=lambda instance: self.add_digit('2')))
        gl.add_widget(Button(text='3', on_press=lambda instance: self.add_digit('3')))
        gl.add_widget(Button(text='+', on_press=lambda instance: self.add_digit('+')))

        gl.add_widget(Widget())
        gl.add_widget(Button(text='0', on_press=lambda instance: self.add_digit('0')))
        gl.add_widget(Button(text='.', on_press=lambda instance: self.add_digit('.')))
        gl.add_widget(Button(text='=', on_press=lambda instance: self.equel()))
        bl.add_widget(gl)
        return bl


if __name__ == '__main__':
    CalculatorApp().run()
