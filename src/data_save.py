import json
import datetime
from pathlib import Path


def dump_data_to_json(entry):
    json_path = Path("Json/Zeitnachweise.json")
    json_path.parent.mkdir(parents=True, exist_ok=True)

    
    if json_path.exists() and json_path.stat().st_size > 0:
        with json_path.open("r", encoding="utf-8") as f:
            daten = json.load(f)
    else:
        daten = {}

    daten[entry["date"]] = entry


    with json_path.open("w", encoding="utf-8") as f:
        json.dump(daten, f, indent=4, ensure_ascii=False)
    


def saving(result, names):
    overtime, result_hours, result_minutes, work_start, work_end = result
    family_name_input, name_input = names
    importet_date = str(datetime.date.today())


    entry = dict(
        familyname = "",
        name = "",
        date = "",
        start_time = "",
        end_time = "",
        houers_worked = "",
        minutes_worked = "",
        over_time = ""
    )

    entry.update({
        "familyname": family_name_input,
        "name": name_input,
        "date": importet_date,
        "start_time": work_start,
        "end_time": work_end,
        "houers_worked": result_hours,
        "minutes_worked": result_minutes,
        "over_time": overtime,
    })
    
    print(json.dumps(entry, indent=4, ensure_ascii=False, default=str))

    dump_data_to_json(entry)
   