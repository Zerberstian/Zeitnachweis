import re

LETTERS_AND_SEPARATORS = re.compile(r"[^\W\d_]+(?:[-'’][^\W\d_]+)*")

### Name Inputs ###
def requesting_name(name_prompt):
    while True:
        name = input(name_prompt).strip()

        if len(name) > 20:
            print("Der Name ist zu lang (maximal 20 Zeichen).")
        elif not LETTERS_AND_SEPARATORS.fullmatch(name):
            print("Bitte gib nur Buchstaben ein.")
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
