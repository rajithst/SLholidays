
import pandas as pd
import datetime

holidays = pd.read_csv("slholidays/data/public_holidays.csv")
days = holidays["public_holidays"]
names = holidays["name"]
holidays_dict = dict(zip(days,names))

holidays_dict.keys()

    
def is_holiday(date):
    inp =  parse_date_to_obj(date)
    date_s = parse_obj_to_string(inp)
    if date_s in holidays_dict.keys():
        return True
    else:
        return False
    
def get_previous_and_next_holiday(date,next_day=True,include_weekends=False):
    pass
    
    
    
    
def parse_obj_to_string(date):
    return datetime.datetime.strftime(date,"%Y-%m-%d")

def parse_date_to_obj(date):
    return datetime.datetime.strptime(date,"%Y-%m-%d")