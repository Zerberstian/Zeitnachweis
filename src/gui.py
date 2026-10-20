import tkinter as tk
import sys

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

BORDERWIDTH = 2
# Fonts
MAINFOND = FONTFAMILY, FONTSICE, FONTSTYLE
FONTFAMILY = "Arial"
FONTSICE = 12
FONTSTYLE = "bold"


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

    context_frame_1 = tk.Frame(root,
        bg=BACKGROUND,
        highlightbackground=BORDERS,
        highlightcolor=BORDERS,
        highlightthickness=BORDERWIDTH
    )
    context_frame_1.grid(row=0, column=1, sticky="nsew")



    context_frame_2 = tk.Frame(root,
        bg="Green",
        highlightbackground=BORDERS,
        highlightcolor=BORDERS,
        highlightthickness=BORDERWIDTH
    )

    active_frame = context_frame_1

    def swap_frames(swap_with):
        nonlocal active_frame

        if active_frame is swap_with:
            return

        active_frame.grid_forget()  
        swap_with.grid(row=0, column=1, sticky="nsew")  
        active_frame = swap_with 

    Context_1_Button = tk.Button(navigation_frame,
                        text="Start",
                        font=('Arial', 12, 'bold'),
                        bg=PRIMARYBUTTONS,
                        fg=PRIMARYBUTTONTEXT,
                        command=lambda: swap_frames(context_frame_1))
    Context_1_Button.pack()


    Context_2_Button = tk.Button(navigation_frame,
                        text="Start",
                        font=('Arial', 12, 'bold'),
                        bg=PRIMARYBUTTONS,
                        fg=PRIMARYBUTTONTEXT,
                        command=lambda: swap_frames(context_frame_2))
    Context_2_Button.pack()
    

    root.mainloop()

if __name__ == "__main__":
    initialize_gui()