import re

def name_request():
    Name = input("Bitte gib deinen Nachnamen ein\n")
    Name2 = input("Bitte gib deinen Namen ein\n")

    return Name, Name2

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

