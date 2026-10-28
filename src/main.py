from Time_calculation import calculating
from output import outputing
from data_save import saving
from flet_gui import SubmittedValues, start_gui


def process_submission(values: SubmittedValues) -> None:
    family_name, middle_name, first_name, start_time, end_time = values
    names_input = (family_name, middle_name, first_name)
    time_inputs = (start_time, end_time)
    calculated_times = calculating(time_inputs)
    outputing(calculated_times)
    saving(calculated_times, names_input)


if __name__ == "__main__":
    start_gui(process_submission)