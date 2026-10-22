from widgets_class import AppButton
import tkinter as tk
from tkinter import ttk
import sys
from User_Input import requesting_name


# using Entry() to get user input

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
MAINFOND = FONTFAMILY, FONTSICE, FONTSTYLE

def initialize_gui():
    
    root= tk.Tk()

    if sys.platform.startswith("linux"):
        root.attributes("-zoomed", True)

    elif sys.platform == "win32":
        root.state("zoomed")

    root.config(bg="Black")
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=10)

    # Frames
    navigation_frame = tk.Frame(
        root,
        bg=BACKGROUND,
        highlightbackground=BORDERS,
        highlightcolor=BORDERS,
        highlightthickness=BORDERWIDTH
    )
    navigation_frame.grid(row=0, column=0, sticky="nsew")
    y = 1
    x = 1
    navigation_frame.grid_columnconfigure(0, weight=1)
    navigation_frame.grid_columnconfigure(1, weight=2)
    navigation_frame.grid_rowconfigure(0, weight=y)
    navigation_frame.grid_rowconfigure(1, weight=x)
    navigation_frame.grid_rowconfigure(2, weight=y)    
    navigation_frame.grid_rowconfigure(3, weight=x) 
    navigation_frame.grid_rowconfigure(4, weight=y)
    navigation_frame.grid_rowconfigure(5, weight=x)
    navigation_frame.grid_rowconfigure(6, weight=y)
    navigation_frame.grid_rowconfigure(7, weight=x)
    navigation_frame.grid_rowconfigure(8, weight=y)
    navigation_frame.grid_rowconfigure(9, weight=x)
    navigation_frame.grid_rowconfigure(10, weight=20)


    context_frame_1 = tk.Frame(root,
        bg=BACKGROUND,
        highlightbackground=BORDERS,
        highlightcolor=BORDERS,
        highlightthickness=BORDERWIDTH)
    context_frame_1.grid(row=0, column=1, sticky="nsew")

    settings_frame = tk.Frame(root,
        bg=BACKGROUND,
        highlightbackground=BORDERS,
        highlightcolor=BORDERS,
        highlightthickness=BORDERWIDTH)


    context_frame_2 = tk.Frame(root,
        bg="Green",
        highlightbackground=BORDERS,
        highlightcolor=BORDERS,
        highlightthickness=BORDERWIDTH)


    context_frame_3 = tk.Frame(root,
        bg="Black",
        highlightbackground=BORDERS,
        highlightcolor=BORDERS,
        highlightthickness=BORDERWIDTH)


    context_frame_4 = tk.Frame(root,
        bg="Yellow",
        highlightbackground=BORDERS,
        highlightcolor=BORDERS,
        highlightthickness=BORDERWIDTH)
    
    active_frame = context_frame_1

    def swap_frames(swap_with):
        nonlocal active_frame

        if active_frame is swap_with:
            return

        active_frame.grid_forget()  
        swap_with.grid(row=0, column=1, sticky="nsew")  
        active_frame = swap_with


    style = ttk.Style(root)
    style.theme_use("clam")
    style.configure(
        "App.TButton",
        font=MAINFOND,
        foreground=PRIMARYBUTTONTEXT,
        background=PRIMARYBUTTONS,
        padding=(12, 8),
    )

    style.map(
        "App.TButton",
        background=[("pressed", "#162B46"),("active", "#2B527F"),],)
    
    settings_button = AppButton(
        navigation_frame,
        text="≡",
        command=lambda: swap_frames(settings_frame),)
    settings_button.grid(row=0, column=0, sticky="nw")


    Context_1_Button = AppButton(navigation_frame,
                                 text="Button 1",
                                 command=lambda: swap_frames(context_frame_1))
    Context_1_Button.grid(row=1, column=1, sticky="nsew")


    Context_2_Button = AppButton(navigation_frame,
                                 text="Button 2",
                                 command=lambda: swap_frames(context_frame_2))
    Context_2_Button.grid(row=3, column=1, sticky="nsew") 
   

    Context_3_Button = AppButton(navigation_frame,
                                 text="Button 3",
                                 command=lambda: swap_frames(context_frame_3))
    Context_3_Button.grid(row=5, column=1, sticky="nsew")  

    Context_4_Button = AppButton(navigation_frame,
                                 text="Button 4",
                                 command=lambda: swap_frames(context_frame_4))
    Context_4_Button.grid(row=7, column=1, sticky="nsew")  

    Exit_Btn = AppButton(navigation_frame,
                                 text="Aus",
                                 command=lambda:sys.exit(0))
    Exit_Btn.grid(row=9, column=1, sticky="nsew")
    

    name_label = tk.Label(context_frame_1, text = 'Username', font=MAINFOND)
    name_label.grid(row=0, column=0)

    name_entry = tk.Entry(context_frame_1, textvariable = "name_var", font=MAINFOND)
    name_entry.grid(row=0, column=1)

    tk.Button(context_frame_1, text="Butt", command=lambda: requesting_name(name_entry)).grid(row=0, column=2)
    #Family_Name

    
    root.mainloop()

if __name__ == "__main__":
    initialize_gui()