import re

LETTERS_AND_SEPARATORS = re.compile(r"[^\W\d_]+(?:[-'’][^\W\d_]+)*")

# Name Inputs
def request_name(prompt):
    while True:
        name = input(prompt).strip()

        if len(name) > 20:
            print("Der Name ist zu lang (maximal 20 Zeichen).")
        elif not LETTERS_AND_SEPARATORS.fullmatch(name):
            print("Bitte gib nur Buchstaben ein.")
        else:
            return name

def name_request():
    family_name = request_name("Bitte gib deinen Nachnamen ein:\n")
    first_name = request_name("Bitte gib deinen Vornamen ein:\n")
    return family_name, first_name

# Time Inputs
def time_request():
    start_time = start_time_request()
    end_time = end_time_request()

    return start_time, end_time

def start_time_request():

    WorkTimeStart = ""
    while WorkTimeStart != re.fullmatch(r"(?:[01]\d|2[0-3]):[0-5]\d", WorkTimeStart):
        
        WorkTimeStart = input("Gib deine Arbeitsbeginn ein (HH:MM): ")

        if re.fullmatch(r"(?:[01]\d|2[0-3]):[0-5]\d", WorkTimeStart):
            print(f"Startzeit: {WorkTimeStart}")

            return WorkTimeStart

        else:
            print("Value Error: Bitte gib eine gültige Uhrzeit ein.")
            
        

def end_time_request():

    WorkTimeEnd = ""
    while WorkTimeEnd != re.fullmatch(r"(?:[01]\d|2[0-3]):[0-5]\d", WorkTimeEnd):
        
        WorkTimeEnd = input("Gib deine Arbeitsende ein (HH:MM): ")

        if re.fullmatch(r"(?:[01]\d|2[0-3]):[0-5]\d", WorkTimeEnd):
            print(f"Endzeit: {WorkTimeEnd}")

            return WorkTimeEnd

        else:
            print("Value Error: Bitte gib eine gültige Uhrzeit ein.")

