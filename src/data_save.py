import json
import datetime

'''
with open("Zeitnachweise.json", "r", encoding="utf-8") as f:
    Zeitnachweise = json.load(f)
'''

def dump(write):
    with open("Json/Zeitnachweise.json", "w", encoding="utf-8") as f:
        json.dump(write, f, indent=4, ensure_ascii=False)

importet_date = str(datetime.date.today())

def saving(result, names):
    overtime, result_hours, result_minutes, work_start, work_end = result
    family_name_input, name_input = names

    dictionary_data = dict(
        familyname = "",
        name = "",
        date = "",
        start_time = "",
        end_time = "",
        houers_worked = "",
        minutes_worked = "",
        over_time = ""
    )

    dictionary_data.update({
        "familyname": family_name_input,
        "name": name_input,
        "date": importet_date,
        "start_time": work_start,
        "end_time": work_end,
        "hours_worked": result_hours,
        "minutes_worked": result_minutes,
        "over_time": overtime,
    })
    
    print(json.dumps(dictionary_data, indent=4, ensure_ascii=False, default=str))

    x = dictionary_data
    dump(x)
   