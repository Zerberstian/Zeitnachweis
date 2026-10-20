import tkinter as tk

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
#Akzent-Fläche        = "#D9F2EE"
SUCCESS = "#166534"
WARNINGCOLOR = "#92400E"
ERRORSCOLOR = "#B42318"

def swap_fames(to_swap, swap_with):
    to_swap.grid_forget()
    swap_with.grid(row=0, column=1, sticky="nsew")

def initialize_gui():

    root= tk.Tk()

    root.state('zoomed') 
    root.config(bg="Black")
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=3)

    Menu_Frame = tk.Frame(root, bg=BACKGROUND)
    Menu_Frame.grid(row=0, column=1, sticky="nsew")

    Main_Frame = tk.Frame(root, bg=BACKGROUND)
    #Menu_Frame.grid(row=0, column=0, sticky="nsew")

    Start_Button = tk.Button(Menu_Frame,
                            text="Start",
                            font=('Arial', 12, 'bold'),
                            bg=PRIMARYBUTTONS,
                            fg=PRIMARYBUTTONTEXT,
                            command=lambda: swap_fames(to_swap=Menu_Frame, swap_with=Main_Frame))
    Start_Button.pack()

    root.mainloop()

if __name__ == "__main__":
    initialize_gui()