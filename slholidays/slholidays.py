import datetime

class holidays:
    
    def __init__(self,data):
        
        self.holidays_dict= data
        
    '''def load_holidays(self,holidays):
        global holidays_dict 
        holidays_dict = holidays
        return holidays_dict'''
    
    def get_all_holidays(self):
        
        if self.holidays_dict is not None:
            return self.holidays_dict
        
    
    def is_holiday(self,date):
        inp =  self.__parse_string_to_obj(date)
        date_s = self.__parse_obj_to_string(inp)
        if date_s in self.holidays_dict.keys():
            return True
        else:
            return False
        
    def get_the_day(self,date):
        date = self.__date_clean_or_today(date)
        return date.strftime("%A")
    
    def holiday_name(self,date):
         
        if self.is_public_holiday(date):
            if isinstance(date,datetime.datetime) is False:
                date = self.__parse_string_to_obj(date)
            return self.holidays_dict.get(self.__parse_obj_to_string(date))
    
    def year_holidays(self,year,include_weekends=False):
        
        date = datetime.datetime(year,1,1)
        all_holidays = self.__get_dates_as_obj()
        if include_weekends is True:
            year_end = datetime.datetime(year,12,31)
            year_weekends = self.get_weekends_between(date,year_end)
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
            year_hols = self.year_holidays(year)
            month_holidays=[]
            for d in year_hols:
                if d.month == date.month:
                    month_holidays.append(d)
            return month_holidays
        
    
    def get_next_holiday(self,date=None,include_weekends=False):
        
        date = self.__date_clean_or_today(date)  
        next_holiday = self.__next_or_prev_holiday_from_list(date,True)
        
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
    
    def number_of_days_to_next_holiday(self,date,include_weekends=False):
        
        date = self.__date_clean_or_today(date)
        next_holiday = self.get_next_holiday(date,include_weekends)
        diff = next_holiday - date
        return diff.days
    
    
        
    def get_previous_holiday(self,date=None,include_weekends=False):
        
        date = self.__date_clean_or_today(date)
        
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
        
    
    def number_of_days_to_previous_holiday(self,date,include_weekends=False):
        
        date = self.__date_clean_or_today(date)
        last_holiday = self.get_previous_holiday(date,include_weekends)
        diff = date -last_holiday
        return diff.days
    
    def number_of_days_between(self,from_date,to_date,include_weekends=True):
        
        number_of_days = len(self.all_days_between(from_date,to_date,include_weekends)) 
        return number_of_days
    
    def all_days_between(self,from_date,to_date,include_weekends=True):
        
        
        f_date = self.__date_clean_or_today(from_date)
        t_date = self.__date_clean_or_today(to_date)
        num = f_date - t_date
        number_of_days = abs(num.days) 
        all_dates_between = [f_date + datetime.timedelta(days=x) for x in range(1,number_of_days+1)]
        if include_weekends is False:
            clean_dates=[]
            for d in all_dates_between:
                if (d.weekday()!=5 and d.weekday()!=6):
                    clean_dates.append(d)
            all_dates_between = clean_dates
        return all_dates_between
    
    def get_weekends_between(self,from_date,to_date):
        
        f_date = self.__date_clean_or_today(from_date)
        t_date = self.__date_clean_or_today(to_date)
        num = f_date - t_date
        number_of_days = abs(num.days) 
        all_dates_between = [f_date + datetime.timedelta(days=x) for x in range(1,number_of_days+1)]
        weekends = [(d) for d in all_dates_between if d.weekday()==5 or d.weekday()==6]
        return weekends
        
        
        
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
        
    def __date_clean_or_today(self,date):
        
        if date is None:
            date = datetime.datetime.today()
        else:
            if isinstance(date,datetime.datetime) is False:
                date = self.__parse_string_to_obj(date)
        return date
    
    def __parse_obj_to_string(self,date):
        return datetime.datetime.strftime(date,"%Y-%m-%d")
    
    
    def __parse_string_to_obj(self,date):
        return datetime.datetime.strptime(date,"%Y-%m-%d")
    
    
    def __get_dates_as_obj(self):
        h_list = self.holidays_dict.keys()
        return [ self.__parse_string_to_obj(x) for x in h_list ]
    
    
