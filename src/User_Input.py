import re
import tkinter as tk

LETTERS_AND_SEPARATORS = re.compile(r"[^\W\d_]+(?:[-'’][^\W\d_]+)*")


#name_var=tk.StringVar()

### Name Inputs ###
def requesting_name(entr):
    while True:
        name = input(entr).strip() #name_var.get()#
        #name = entr.get()
        
        if len(name) > 20:
            print("Der Name ist zu lang (maximal 20 Zeichen).")
            #entr.delete(0,len(name))
            #entr.insert(0,"")
        elif not LETTERS_AND_SEPARATORS.fullmatch(name) and name != "":
            print("Bitte gib nur Buchstaben ein.")
            #entr.delete(0,len(name))
            #entr.insert(0,"")
        else:
            return name

def name_request():
    family_name = requesting_name("Bitte gib deinen Nachnamen ein:\n")
    first_name = requesting_name("Bitte gib deinen Vornamen ein:\n")

    return family_name, first_name

### Time Inputs ###
def time_request(time_prompt):  
    while True:
        time = input(time_prompt).strip()

        if not re.fullmatch(r"(?:[01]\d|2[0-3]):[0-5]\d", time):
            print("Gib nur eine Uhrzeit im Format HH:MM ein")
        else:
            return time
        
def requesting_time():
    start_time = time_request("Gib deine Arbeitsbeginn ein (HH:MM): ")
    end_time = time_request("Gib deine Arbeitsende ein (HH:MM): ")

    return start_time, end_time
