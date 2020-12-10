from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config

Config.set('graphics', 'resizable', 0)
Config.set('graphics', "width", 200)
Config.set('graphics', "height", 300)

class CalculationApp(App):

    def results(self, instance):
        self.lbl.text = str(eval(self.lbl.text))
        self.formula = "0"

    

    def update_label(self):
       self.lbl.text= self.formula 

    def clr_lbl(self, instance):
        self.formula = "0"

    def add_number (self, instance):
        if (self.formula == "0"):
            self.formula = ""
        elif (self.formula == ","):
            self.formula = "0,"
        elif (self.formula == "+/-"):
            self.formula += "-"
        
        self.formula += str(instance.text)
        self.update_label()
        
    def add_operation(self, instance):
        if (str(instance.text).lower()=="x"):
            self.formula += "*"
        else:
            self.formula += str(instance.text)
        self.update_label()

    def build (self):
        self.formula = "0"
        bl = BoxLayout(orientation = "vertical", padding = 5)
        self.lbl = Label(text="0", halign = "right", valign="center" , text_size = (200-10, 300*.35-10), font_size = 40, size_hint = (1, .35))
       
        bl.add_widget(self.lbl)

        gl = GridLayout(cols = 4, spacing =2, size_hint = (1, .65))

        gl.add_widget(Button(text = "CE", on_press = self.clr_lbl)) 
        gl.add_widget(Button(text = "C",)) 
        gl.add_widget(Button(text = "<x]",))
        gl.add_widget(Button(text = "/", on_press = self.add_operation)) 

        gl.add_widget(Button(text = "7", on_press = self.add_number)) 
        gl.add_widget(Button(text = "8", on_press = self.add_number)) 
        gl.add_widget(Button(text = "9", on_press = self.add_number))
        gl.add_widget(Button(text = "x", on_press = self.add_operation)) 

        gl.add_widget(Button(text = "4", on_press = self.add_number))
        gl.add_widget(Button(text = "5", on_press = self.add_number))
        gl.add_widget(Button(text = "6", on_press = self.add_number))
        gl.add_widget(Button(text = "-", on_press = self.add_operation)) 

        gl.add_widget(Button(text = "1", on_press = self.add_number))
        gl.add_widget(Button(text = "2", on_press = self.add_number))
        gl.add_widget(Button(text = "3", on_press = self.add_number))
        gl.add_widget(Button(text = "+", on_press = self.add_operation)) 

        gl.add_widget(Button(text = "+/-", on_press = self.add_number))
        gl.add_widget(Button(text = "0", on_press = self.add_number))
        gl.add_widget(Button(text = ",", on_press = self.add_number))
        gl.add_widget(Button(text = "=", on_press = self.results))  
        
        bl.add_widget(gl)
        return bl

if __name__ == "__main__":
    CalculationApp().run()