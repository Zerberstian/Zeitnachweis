from User_Input import start_time_request, end_time_request
import sys

PAUSENZEIT = 45

def calculating():

    work_start = start_time_request().split(":")
    work_end = end_time_request().split(":")
    
    work_start_hours = int(work_start[0])
    work_start_minutes = int(work_start[1])

    work_end_hours = int(work_end[0])
    work_end_minutes = int(work_end[1])

    start_total_minutes = (work_start_hours * 60) + work_start_minutes
    end_total_minutes = (work_end_hours * 60) + work_end_minutes

    work_Time_Result = end_total_minutes - start_total_minutes - PAUSENZEIT

    if work_Time_Result < 0:
        print(f"Fehler: Du hast weniger als Pausenzeit ({PAUSENZEIT}) Minuten gearbeitet")

        while True:
            correction = input(f"Möchtest du nochmal korrigieren? (j/n)\n").strip().lower()
            
            if correction == "j":
                calculating()
                return
            
            elif correction == "n":
                print("Programm schließt...")
                sys.exit(1)
            
            else:
                print("Fehler bei der Eingabe - bitte j oder n eingeben")
        
    else:
        result_hours = work_Time_Result // 60
        result_minutes = work_Time_Result % 60
        print(f"Resultat: {result_hours} Stunden und {result_minutes} Minuten")
        
    overtime = -(480 - work_Time_Result) 

    return overtime, result_hours, result_minutes
