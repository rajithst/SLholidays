# -*- coding: utf-8 -*-

import slholidays
from slholidays.data import seed
slh = seed.load_sl_public_holidays() 

slholidays.load_holidays(slh)

allh = slholidays.get_all_holidays()
h=slholidays.get_next_holiday("2019-5-1",include_weekends=False)
r1 = slholidays.get_previous_holiday("2019-5-1",include_weekends=False)

hl = slholidays.holiday_name("2019-4-14")
h2 = slholidays.is_public_holiday("2019-5-2")
r2 = slholidays.number_of_days_to_next_holiday("2019-5-1",include_weekends=True)
r3 = slholidays.number_of_days_to_previous_holiday("2019-5-1",include_weekends=True)
d = slholidays.get_the_day("2019-04-14")
nm = slholidays.number_of_days_between("2019-01-15","2019-04-14",include_weekends=True)
alldays = slholidays.all_days_between("2019-01-15","2019-04-14",include_weekends=False)