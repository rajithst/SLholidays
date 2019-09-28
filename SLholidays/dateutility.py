# -*- coding: utf-8 -*-
import datetime

        
def _validate_dtype(date,dtype=str):
    
    if isinstance(date,datetime.datetime) is False:
        date = _parse_string_to_obj(date)
    return date

def _parse_obj_to_string(date):
    return datetime.datetime.strftime(date,"%Y-%m-%d")


def _parse_string_to_obj(date):
    return datetime.datetime.strptime(date,"%Y-%m-%d")

def _parse_format(date):
    return date.strftime('%Y-%m-%d')
        
    