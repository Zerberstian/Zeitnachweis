PAUSENZEIT = 45

def calculating(time_inputs):
    work_start_input, work_end_input = time_inputs

    work_start_hours, work_start_minutes = map(int, work_start_input.split(":"))
    work_end_hours, work_end_minutes = map(int, work_end_input.split(":"))

    start_total_minutes = (work_start_hours * 60) + work_start_minutes
    end_total_minutes = (work_end_hours * 60) + work_end_minutes
    work_time_result = end_total_minutes - start_total_minutes - PAUSENZEIT

    if work_time_result <= 0:
        raise ValueError(
            f"Fehler: Du hast weniger als die Pausenzeit "
            f"({PAUSENZEIT} Minuten) gearbeitet."
        )

    result_hours = work_time_result // 60
    result_minutes = work_time_result % 60
    overtime = -(480 - work_time_result)

    return (
        overtime,
        result_hours,
        result_minutes,
        work_start_input,
        work_end_input,
    )
