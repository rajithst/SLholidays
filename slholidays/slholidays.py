
import pandas as pd
import datetime

holidays = pd.read_csv("slholidays/data/public_holidays.csv")
days = holidays["public_holidays"]
names = holidays["name"]
holidays_dict = dict(zip(days,names))

holidays_dict.keys()

    
def is_holiday(date):
    inp =  datetime.datetime.strptime(date,"%Y-%m-%d")
    date_s = datetime.datetime.strftime(inp,"%Y-%m-%d")
    if date_s in holidays_dict.keys():
        return True
    else:
        return False