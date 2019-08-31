# -*- coding: utf-8 -*-
import datetime

class util_dates:
    
    today = datetime.datetime.today()
        
    def date_clean_or_today(self,date):
        
        if date is None:
            date = self.today
        else:
            if isinstance(date,datetime.datetime) is False:
                date = self.parse_string_to_obj(date)
        return date
    
    def parse_obj_to_string(self,date):
        return datetime.datetime.strftime(date,"%Y-%m-%d")
    
    
    def parse_string_to_obj(self,date):
        return datetime.datetime.strptime(date,"%Y-%m-%d")
    
    
    