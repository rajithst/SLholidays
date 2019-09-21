# -*- coding: utf-8 -*-
import datetime

        
def _validate_dtype(date,dtype=str):
    
    if isinstance(date,datetime.datetime) is False:
        if isinstance(dtype,str):
            date = __parse_string_to_obj(date)
    date = __parse_format(date)        
    return date

def __parse_obj_to_string(date):
    return datetime.datetime.strftime(date,"%Y-%m-%d")


def __parse_string_to_obj(date):
    return datetime.datetime.strptime(date,"%Y-%m-%d")

def __parse_format(date):
    return date.strftime('%Y-%m-%d')
        
    