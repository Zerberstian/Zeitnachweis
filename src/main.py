from Time_calculation import calculating
from output import outputing
from data_save import saving
from User_Input import name_request, requesting_time

if __name__ == "__main__":
    names_input = name_request()
    time_inputs = requesting_time()
    calculated_times = calculating(time_inputs)
    outputing(calculated_times)
    saving(calculated_times, names_input)