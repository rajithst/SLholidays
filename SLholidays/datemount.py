# -*- coding: utf-8 -*-
import datetime

class date_mount:
        
    def number_of_days_between(self,from_date,to_date,include_weekends=True):
        
        number_of_days = len(self.all_days_between(from_date,to_date,include_weekends)) 
        return number_of_days
    
    def get_weekends_between(self,from_date,to_date):
        
        f_date = self.__date_clean_or_today(from_date)
        t_date = self.__date_clean_or_today(to_date)
        num = f_date - t_date
        number_of_days = abs(num.days) 
        all_dates_between = [f_date + datetime.timedelta(days=x) for x in range(1,number_of_days+1)]
        weekends = [(d) for d in all_dates_between if d.weekday()==5 or d.weekday()==6]
        return weekends
    
    
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
    
    def is_weekend(self,date):
         date = self.__date_clean_or_today(date)
         if date.weekday()== 5 or date.weekday()==6:
             return True
         else:
            return False
        
        
    def get_the_day(self,date):
        date = self.__date_clean_or_today(date)
        return date.strftime("%A")