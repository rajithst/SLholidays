import datetime
from slholidays.data import seed

holidays_dict = seed.load_holidays()
    
def is_public_holiday(date):
    inp =  __parse_string_to_obj(date)
    date_s = __parse_obj_to_string(inp)
    if date_s in holidays_dict.keys():
        return True
    else:
        return False
    
def get_next_holiday(date=None,include_weekends=False):
 
    if date is None:
        date = datetime.datetime.today()
    else:
        date = __parse_string_to_obj(date)
    
    holiday_list_objects = __get_dates_as_obj()
    
    if date in holiday_list_objects:
        idx = holiday_list_objects.index(date)
        return holiday_list_objects[idx+1]
    else:
        next_dates = [ (d) for d in holiday_list_objects if d > date]
        return next_dates[0]
        
    
def get_previous_holiday(date=datetime.datetime.today(),include_weekends=False):
    pass
    
    
    
def __parse_obj_to_string(date):
    return datetime.datetime.strftime(date,"%Y-%m-%d")

def __parse_string_to_obj(date):
    return datetime.datetime.strptime(date,"%Y-%m-%d")

def __get_dates_as_obj():
    h_list = holidays_dict.keys()
    return [ __parse_string_to_obj(x) for x in h_list ]


