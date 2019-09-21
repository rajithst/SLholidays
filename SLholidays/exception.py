# -*- coding: utf-8 -*-

__DATA_VALUE_ERROR = "Holidays data is not defined."
__DICT_TYPE_ERROR = "Data must be dictionary format"
__ARGUMENT_MISSING_ERROR = "Date argument is not passed"

def _arg_missing():
    return __ARGUMENT_MISSING_ERROR

def _data_missing():
    return __DATA_VALUE_ERROR

def _data_type_error():
    return __DICT_TYPE_ERROR