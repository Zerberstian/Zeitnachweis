from User_Input import Input_request

PAUSENZEIT = 45

def placeholder():

    work_start = Input_request()[0]
    work_end = Input_request()[1]

    work_start.split(":")
    work_end.split(":")
    
    work_start_hours = int(work_start[0])
    work_start_minutes = int(work_start[1])

    work_end_hours = int(work_end[0])
    work_end_minutes = int(work_end[1])

    work_Time_Result = work_end_hours - work_start_hours 


    print(work_Time_Result)