import datetime
import SLholidays.dateutility as util
import  SLholidays.exception as exp
from SLholidays.datemount import date_mount

class holidays:
    
    def __init__(self,data):
        
        if data is None:
            raise ValueError(exp._arg_missing)
        else:
            if isinstance(data,dict):
                self.holidays_dict= data
            else:
                raise TypeError(exp._data_type_error)
    
    def get_all_holidays(self):
        
        if self.holidays_dict is not None:
            return self.holidays_dict
        else:
            raise ValueError(exp._data_type_error)
        
    
    def is_holiday(self,date):
        
        if date is None:
            raise ValueError(exp._arg_missing)
        else:    
            inp =  util._validate_dtype(str,date)
            
        if inp in self.holidays_dict.keys():
            return True
        else:
            return False

    
    def holiday_name(self,date):
         
        if self.is_holiday(date):
            date = util._validate_dtype(str,date)
            return self.holidays_dict.get(date)
        else:
            return False
        
    def year_holidays(self,year,include_weekends=False):
        
        date = datetime.datetime(year,1,1)
        all_holidays = self.__get_dates_as_obj()
        if include_weekends is True:
            year_end = datetime.datetime(year,12,31)
            year_weekends = date_mount.get_weekends_between(date,year_end)
            f = set(year_weekends)
            s = set(all_holidays)
            all_holidays = sorted(f.union(s))
            
        year_holidays = []
        for d in all_holidays:
            if d.year==date.year:
                year_holidays.append(d)
        return year_holidays
    
    def month_holidays(self,year,month,include_weekends=False):
        date = datetime.date(year,month,1)
        if year is not None:
            year_hols = self.year_holidays(year,include_weekends)
            month_holidays=[]
            for d in year_hols:
                if d.month == date.month:
                    month_holidays.append(d)
            return month_holidays
        
    def week_holidays(self,date):
        pass
        
        
    
    def get_next_holiday(self,date=None,include_weekends=False):
        
        date = util._validate_dtype(date=date)  
        next_holiday = self.__next_or_prev_holiday_from_list(date,next_h=True)
        
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
    
            
    def get_previous_holiday(self,date=None,include_weekends=False):
        
        date = util.ate_clean_or_today(date)
        
        last_holiday = self.__next_or_prev_holiday_from_list(date,False)
        
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
    
    def number_of_days_to_next_holiday(self,date,include_weekends=False):
        
        date = util._validate_dtype(date=date)
        next_holiday = self.get_next_holiday(date,include_weekends)
        diff = next_holiday - date
        return diff.days
        
    
    def number_of_days_to_previous_holiday(self,date,include_weekends=False):
        
        date = util._validate_dtype(date=date)
        last_holiday = self.get_previous_holiday(date,include_weekends)
        diff = date -last_holiday
        return diff.days
    
        
    def __next_or_prev_holiday_from_list(self,date,next_h):
        
        holiday_list_objects = self.__get_dates_as_obj()
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
    
    def __get_dates_as_obj(self):
        h_list = self.holidays_dict.keys()
        dates = [ util._validate_dtype(date=x) for x in h_list ]
        return sorted(dates)
