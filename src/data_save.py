import json
import datetime

x = datetime.date.today()

def saving(result, names):
    overtime, result_hours, result_minutes, work_start, work_end = result
    family_name_input, name_input = names

    data = dict(
        familyname = "",
        name = "",
        date = "",
        start_time = "",
        end_time = "",
        houers_worked = "",
        minutes_worked = "",
        over_time = ""
    )

    data.update({
        "familyname": family_name_input,
        "name": name_input,
        "date": x,
        "start_time": work_start,
        "end_time": work_end,
        "hours_worked": result_hours,
        "minutes_worked": result_minutes,
        "over_time": overtime,
    })
    
    print(json.dumps(data, indent=4, ensure_ascii=False, default=str))
   