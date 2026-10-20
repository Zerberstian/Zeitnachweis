from Time_calculation import calculating
from output import outputing
from data_save import saving
from User_Input import name_request

if __name__ == "__main__":
    names = name_request()
    result = calculating()
    outputing(result)
    saving(result, names)