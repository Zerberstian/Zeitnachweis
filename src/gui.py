import tkinter as tk
import sys

# using Entry() to get user input
BACKGROUND = "#F3F5F7"
ENTRIES = "#FFFFFF"
PRIMARYTEXT = "#1F2937"
SECONDARYTEXT = "#5B6573"
BORDERS = "#D6DCE3"
PRIMARYBUTTONS = "#1F3A5F"
PRIMARYBUTTONTEXT = "#FFFFFF"
#Akzent / Zweitbutton = "#0F766E"
#Akzent-Text          = "#FFFFFF"
ACCENTS = "#D9F2EE"
SUCCESS = "#166534"
WARNINGCOLOR = "#92400E"
ERRORSCOLOR = "#B42318"

def swap_fames(to_swap, swap_with):
    to_swap.grid_forget()
    swap_with.grid(row=0, column=1, sticky="nsew")

def initialize_gui():

    root= tk.Tk()

    if sys.platform.startswith("linux"):
        root.attributes("-zoomed", True)

    elif sys.platform == "win32":
        root.state("zoomed")

    root.config(bg="Black")
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=3)

    # Frames
    navigation_frame = tk.Frame(
        root,
        bg=ACCENTS,
        highlightbackground=BORDERS,
        highlightcolor=BORDERS,
        highlightthickness=5
    )
    navigation_frame.grid(row=0, column=0, sticky="nsew")

    context_frame_1 = tk.Frame(root,
        bg=BACKGROUND,
        highlightbackground=BORDERS,
        highlightcolor=BORDERS,
        highlightthickness=5
    )
    context_frame_1.grid(row=0, column=1, sticky="nsew")

    context_frame_2 = tk.Frame(root,
        bg=BACKGROUND,
        highlightbackground=BORDERS,
        highlightcolor=BORDERS,
        highlightthickness=5
    )

    Start_Button = tk.Button(navigation_frame,
                            text="Start",
                            font=('Arial', 12, 'bold'),
                            bg=PRIMARYBUTTONS,
                            fg=PRIMARYBUTTONTEXT,
                            command=lambda: swap_fames(to_swap=context_frame_1, swap_with=context_frame_2))
    Start_Button.pack()

    root.mainloop()

if __name__ == "__main__":
    initialize_gui()