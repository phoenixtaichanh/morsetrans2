from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
class MyGridLayout(GridLayout):
    def __init__(self,**kwargs):
        super(MyGridLayout, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='input:'))
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)
        self.submit=Button(text='done',font_size=32)
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)
    def press(self,instance):
        morse=self.name.text
        if morse == '.....':
            morse='5'
        elif morse == '-...':
            morse='B'
        elif morse == '-.-.':
            morse='C'
        elif morse == '-..':
            morse='D'
        elif morse == '.':
            morse='E'
        elif morse == '..-.':
            morse='F'
        elif morse == '--.':
            morse='G'
        elif morse == '....':
            morse='H'
        elif morse == '..':
            morse='I'
        elif morse == '.---':
            morse='J'
        elif morse == '-.-':
            morse='K'
        elif morse == '.-..':
            morse='L'
        elif morse == '--':
            morse='M'
        elif morse == '-.':
            morse='N'
        elif morse == '---':
            morse='O'
        elif morse == '.--.':
            morse='P'
        elif morse == '--.-':
            morse='Q'
        elif morse == '.-.':
            morse='R'
        elif morse == '...':
            morse='S'
        elif morse == '-':
            morse='T'
        elif morse == '..-':
            morse='U'
        elif morse == '...-':
            morse='V'
        elif morse == '.--':
            morse='W'
        elif morse == '-..-':
            morse='X'
        elif morse == '-.--':
            morse='Y'
        elif morse == '--..':
            morse='Z'
        elif morse == '.----':
            morse='1'
        elif morse == '..---':
            morse='2'
        elif morse == '...--':
            morse='3'
        elif morse == '....-':
            morse='4'
        elif morse == '-....':
            morse='6'
        elif morse == '--...':
            morse='7'
        elif morse == '---..':
            morse='8'
        elif morse == '----.':
            morse='9'
        elif morse == '-----':
            morse='0'

        self.add_widget(Label(text=f'{morse}'))
class MyApp(App):
    def build(self):
        return MyGridLayout()
#runapp
if __name__=="__main__":
    app=MyApp()
    app.run()