# -*- coding: utf-8 -*-
import datetime
import calendar
import SLholidays.dateutility  as util

class date_mount:
    
    def get_the_day(self,date):
        date = util._validate_dtype(date=date)  
        return date.strftime("%A")
    
    def is_weekend(self,date):
         date = util._validate_dtype(date=date)  
         if date.weekday()== 5 or date.weekday()==6:
             return True
         else:
            return False

    def number_of_days_between(self,from_date,to_date,include_weekends=True):
        
        number_of_days = len(self.all_days_between(from_date,to_date,include_weekends)) 
        return number_of_days
    
    def get_weekends_between(self,from_date,to_date):
        
        f_date = util._validate_dtype(date=from_date)
        t_date = util._validate_dtype(date=to_date)
        num = f_date - t_date
        number_of_days = abs(num.days) 
        all_dates_between = [f_date + datetime.timedelta(days=x) for x in range(1,number_of_days+1)]
        weekends = [(d) for d in all_dates_between if self.is_weekend(d)]
        return weekends
    
    
    def all_days_between(self,from_date,to_date,include_weekends=True):
        
        
        f_date = util._validate_dtype (date=from_date)
        t_date = util._validate_dtype (date=to_date)
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
    
    def days_of_week(self,date,include_weekends=True):
        
        date = util._validate_dtype(str,date)
        start_date = datetime.datetime(date.year,date.month,1)
        ndays = calendar.monthrange(date.year,date.month)[1]
        end_date = datetime.datetime(date.year,date.month,ndays)
        return self.all_days_between(start_date,end_date,include_weekends)

    
    def days_of_month(self,date,include_weekends=True):
        date = util._validate_dtype(str,date)
        start_date = datetime.datetime(date.year,date.month,1)
        ndays = calendar.monthrange(date.year,date.month)[1]
        end_date = datetime.datetime(date.year,date.month,ndays)
        return self.all_days_between(start_date,end_date,include_weekends)
            
        
    
    def days_of_year(self,date,include_weekends=True):
        
        date = util._validate_dtype(str,date)
        start_date = datetime.datetime(date.year,1,1)
        end_date = datetime.datetime(date.year,12,31)
        return self.all_days_between(start_date,end_date,include_weekends)
        
    
            
        
  