import re
import json
import datetime
from pathlib import Path


def split_names(names):
    if len(names) == 2:
        family_name, first_name = names
        middle_name = ""
    elif len(names) == 3:
        family_name, middle_name, first_name = names
    else:
        raise ValueError(
            "Names must contain a family name, optional middle name, and first name."
        )

    return family_name, middle_name, first_name


def safe_filename_part(value):
    return re.sub(r"[^\w-]", "_", str(value), flags=re.UNICODE).strip("_")

def dump_data_to_json(entry, names):
    family_name_input, middle_name_input, name_input = split_names(names)

    filename_parts = [family_name_input]
    if middle_name_input:
        filename_parts.append(middle_name_input)
    filename_parts.append(name_input)
    filename = "_".join(safe_filename_part(part) for part in filename_parts) + ".json"
    json_path = Path("Json") / filename
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
    family_name_input, middle_name_input, name_input = split_names(names)
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
        "middle_name": middle_name_input,
        "name": name_input,
        "date": importet_date,
        "start_time": work_start,
        "end_time": work_end,
        "houers_worked": result_hours,
        "minutes_worked": result_minutes,
        "over_time": overtime,
    })
    
    print(json.dumps(entry, indent=4, ensure_ascii=False, default=str))

    dump_data_to_json(entry, names)
   