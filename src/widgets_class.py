import tkinter as tk
from tkinter import ttk

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


class AppFrame(tk.Button):
    def __init__(self, parent, **kwargs):
        super().__init__(
            parent,
            font=MAINFONT,
            bg=PRIMARYBUTTONS,
            fg=PRIMARYBUTTONTEXT,
            **kwargs,
        )


class AppButton(ttk.Button):
    def __init__(self, parent, text, command, **kwargs):
        super().__init__(
            parent,
            text=text,
            command=command,
            style="App.TButton",
            **kwargs,
        )
