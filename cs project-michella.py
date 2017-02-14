import turtle
from turtle_chat_client import Client
from turtle_chat_widgets import Button
from turtle_chat_widgets import TextInput

class TextBox(TextInput):
    def draw_box(self):
        self.draw=turtle.clone()
        self.draw.hideturtle()
        self.draw.penup()
        self.draw.goto(self.width/2,0)
        self.draw.pendown()
        self.draw.goto(-self.width/2,0)
        self.draw.goto(-self.width/2,-self.height)
        self.draw.goto(self.width/2,0)
    def write_msg(self):
        self.writer.clear()
        self.writer.write(self.new_msg)
        
        

