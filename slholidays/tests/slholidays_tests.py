# -*- coding: utf-8 -*-
from unittest import TestCase
from slholidays import slholidays
from slholidays.data import seed

data = seed.load_sl_public_holidays()
slholidays.load_holidays(data)

def test_get_all_holidays():
    s = slholidays.get_all_holidays()
    assert s==data
    
def test_is_public_holiday():
    s = slholidays.is_public_holiday("2019-05-01")
    t = slholidays.is_public_holiday("2019-10-10")
    assert s==True
    assert t==False