from User_Input import start_time_request, end_time_request

PAUSENZEIT = 45

def placeholder():

    work_start = start_time_request().split(":")
    work_end = end_time_request().split(":")

    
    work_start_hours = int(work_start[0])
    work_start_minutes = int(work_start[1])

    work_end_hours = int(work_end[0])
    work_end_minutes = int(work_end[1])

    print(f"{work_end_hours} - {work_start_hours}")

    work_Time_Result = work_end_hours - work_start_hours 


    print(work_Time_Result)