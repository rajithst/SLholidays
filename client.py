# -*- coding: utf-8 -*-

from SLholidays import Holidays
from SLholidays.data import seed
slh = seed.load_sl_public_holidays() 
other = {"2018-04-14":"abc","2018-05-01":"abd"}
dt = dict(slh,**other)


api = Holidays(dt)

api.get_all_holidays()
api.is_holiday("2019-01-20")
api.week_holidays("2019-05-17")
api.month_holidays(year=2019,month=5,include_weekends=True)
api.year_holidays(2019,include_weekends=False)

api.get_weekends_between("2019-08-01","2019-09-01")
api.get_next_holiday("2019-5-1",include_weekends=False)
api.get_previous_holiday("2019-5-1",include_weekends=False)
api.holiday_name("2019-4-14")

api.number_of_days_to_next_holiday("2019-5-1",include_weekends=False)
api.number_of_days_to_previous_holiday("2019-5-1",include_weekends=False)
api.all_days_between("2019-01-15","2019-04-14",include_weekends=False)
api.get_the_day("2019-04-14")
api.number_of_days_between("2019-01-15","2019-04-14",include_weekends=True)
api.get_weekends_between(from_date="2020-08-01",to_date="2020-08-30")