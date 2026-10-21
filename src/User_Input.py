import re

def name_request():
    Familyname = Request_family_name()
    FirstName = Request_first_name()

    return Familyname, FirstName

def Request_family_name():
    loop = True
    while loop == True:
        Familyname = input("Bitte gib deinen Nachnamen ein\n")
        if len(Familyname) <= 20:
            loop = False
            return Familyname
        
        else:
            print("Der angegebener Name ist zu lang.")

def Request_first_name():
    loop = True
    while loop == True:
        Firstname = input("Bitte gib deinen Vornamen ein\n")
        if len(Firstname) <= 20:
            loop = False
            return Firstname
        
        else:
            print("Der angegebener Name ist zu lang.")

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

name_request()