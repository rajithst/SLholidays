# -*- coding: utf-8 -*-
import datetime

class util_dates:
    
    today = datetime.datetime.today()
        
    def _validate_dtype(self,date,dtype=datetime.datetime):
        
        if date is None:
            date = self.today
        else:
            if isinstance(date,datetime.datetime) is False:
                date = self.__parse_string_to_obj(date)
            else:
                date = self.__parse_format(date)
            
        if isinstance(dtype,str):
            date = self.__parse_obj_to_string(date)
        return date
    
    def __parse_obj_to_string(self,date):
        return datetime.datetime.strftime(date,"%Y-%m-%d")
    
    
    def __parse_string_to_obj(date):
        return datetime.datetime.strptime(date,"%Y-%m-%d")
    
    def __parse_format(date):
        return date.strftime('%Y-%m-%d')
        
    