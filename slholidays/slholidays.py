import datetime

def load_holidays(holidays):
    global holidays_dict 
    holidays_dict = holidays
    return holidays_dict

def get_all_holidays():
    if holidays_dict is not None:
        return holidays_dict

def is_public_holiday(date):
    inp =  __parse_string_to_obj(date)
    date_s = __parse_obj_to_string(inp)
    if date_s in holidays_dict.keys():
        return True
    else:
        return False
    
def get_the_day(date):
    date = __date_clean_or_today(date)
    return date.strftime("%A")
    
def holiday_name(date):
     
    if is_public_holiday(date):
        if isinstance(date,datetime.datetime) is False:
            date = __parse_string_to_obj(date)
        return holidays_dict.get(__parse_obj_to_string(date))
        
        
def get_next_holiday(date=None,include_weekends=False):
    
    date = __date_clean_or_today(date)  
    next_holiday = __next_or_prev_holiday_from_list(date,True)
    
    if include_weekends:
            day_number = date.weekday()
            if day_number < 5:
                for_next_weekend = 5-day_number
                next_weekend = date + datetime.timedelta(days=for_next_weekend)
            if day_number == 5:
                next_weekend = date + datetime.timedelta(days=1)
            if day_number==6:
                next_weekend = date + datetime.timedelta(days=6)
            
            if next_holiday > next_weekend:
                next_holiday = next_weekend
    
    return next_holiday

def number_of_days_to_next_holiday(date,include_weekends=False):
    
    date = __date_clean_or_today(date)
    next_holiday = get_next_holiday(date,include_weekends)
    diff = next_holiday - date
    return diff.days


    
def get_previous_holiday(date=None,include_weekends=False):
    
    date = __date_clean_or_today(date)
    
    last_holiday = __next_or_prev_holiday_from_list(date,False)
    
    if include_weekends:
            day_number = date.weekday()
            if day_number < 5:
                for_last_weekend = 5-day_number
                last_weekend = date - datetime.timedelta(days=for_last_weekend)
            if day_number == 5:
                last_weekend = date - datetime.timedelta(days=6)
            if day_number==6:
                last_weekend = date - datetime.timedelta(days=1)
            
            if last_holiday < last_weekend:
                last_holiday = last_weekend
    
    return last_holiday
    

def number_of_days_to_previous_holiday(date,include_weekends=False):
    
    date = __date_clean_or_today(date)
    last_holiday = get_previous_holiday(date,include_weekends)
    diff = date -last_holiday
    return diff.days

def __next_or_prev_holiday_from_list(date,next_h):
    
    holiday_list_objects = __get_dates_as_obj()
    if date in holiday_list_objects:
        idx = holiday_list_objects.index(date)
        if next_h:
            return holiday_list_objects[idx+1]
        else:
            return holiday_list_objects[idx-1]
    else:
        if next_h:
            next_dates = [ (d) for d in holiday_list_objects if d > date]
            return next_dates[0]
        else:
            next_dates = [ (d) for d in holiday_list_objects if d < date]
            return next_dates[len(next_dates)-1]
    
def __date_clean_or_today(date):
    
    if date is None:
        date = datetime.datetime.today()
    else:
        if isinstance(date,datetime.datetime) is False:
            date = __parse_string_to_obj(date)
    return date

def __parse_obj_to_string(date):
    return datetime.datetime.strftime(date,"%Y-%m-%d")


def __parse_string_to_obj(date):
    return datetime.datetime.strptime(date,"%Y-%m-%d")


def __get_dates_as_obj():
    h_list = holidays_dict.keys()
    return [ __parse_string_to_obj(x) for x in h_list ]


