import tkinter as tk

BACKGROUND = "#F3F5F7"
ENTRIES = "#FFFFFF"
PRIMARYTEXT = "#1F2937"
SECONDARYTEXT = "#5B6573"
# Borders
BORDERS = "#D6DCE3"
BORDERWIDTH = 2

PRIMARYBUTTONS = "#1F3A5F"
PRIMARYBUTTONTEXT = "#FFFFFF"

#Akzent / Zweitbutton = "#0F766E"
#Akzent-Text          = "#FFFFFF"

ACCENTS = "#D9F2EE"

# Message Colos
SUCCESS = "#166534"
WARNINGCOLOR = "#92400E"
ERRORSCOLOR = "#B42318"


# Fonts
FONTFAMILY = "Arial"
FONTSICE = 12
FONTSTYLE = "bold"
MAINFONT = FONTFAMILY, FONTSICE, FONTSTYLE


class AppButton(tk.Button):
    def __init__(self, parent, text, command, **kwargs):
        super().__init__(
            parent,
            text=text,
            command=command,
            font=MAINFONT,
            bg=PRIMARYBUTTONS,
            fg=PRIMARYBUTTONTEXT,
            **kwargs,
        )

'''
class Widget:
    def __init__(self, master):
        self.master = master
        self.bg = BACKGROUND
        self.border = BORDERS

class Frame(Widget):
    def __init__(self, master, bg):
        super().__init__(master, bg)  
        

class Button(Widget):
    def __init__(self, master, text, bg, width):
        super().__init__(master, bg)  
        self.width = width
        self.text = text
        self.fornt = ('Arial', 12, 'bold')
        self.bg=PRIMARYBUTTONS
        self.fg=PRIMARYBUTTONTEXT
'''