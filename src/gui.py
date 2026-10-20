import tkinter as tk

# using Entry() to get user input

def initialize_gui():

    root= tk.Tk()

    root.state('zoomed') 

    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    Menu_Frame = tk.Frame(root, bg="black")

    Menu_Frame.grid(row=0, column=0, sticky="nsew")


    root.mainloop()

if __name__ == "__main__":
    initialize_gui()