# -*- coding: utf-8 -*-

import slholidays


data = {'2019-01-15': 'Tamil Thai Pongal Day ',
     '2019-01-20': 'Duruthu Full Moon Poya Day ',
     '2019-02-04': 'National Day ',
     '2019-02-19': 'Navam Full Moon Poya Day ',
     '2019-03-04': 'Mahasivarathri Day ',
     '2019-03-20': 'Madin Full Moon Poya Day ',
     '2019-04-13': 'Day prior to Sinhala & Tamil New Year Day ',
     '2019-04-14': 'Sinhala & Tamil New Year Day ',
     '2019-04-19': 'Good Friday ',
     '2019-05-01': 'May Day ',
     '2019-05-18': 'Vesak Full Moon Poya Day ',
     '2019-05-19': 'Day following Vesak Full Moon Poya Day ',
     '2019-06-05': 'Id Ul-Fitr ',
     '2019-06-16': 'Poson Full Moon Poya Day ',
     '2019-07-16': 'Esala Full Moon Poya Day ',
     '2019-08-12': 'Id Ul-Alha ',
     '2019-08-14': 'Nikini Full Moon Poya Day ',
     '2019-09-13': 'Binara Full Moon Poya Day ',
     '2019-10-13': 'Vap Full Moon Poya Day ',
     '2019-10-27': 'Deepavali ',
     '2019-11-10': 'Milad un-Nabi ',
     '2019-11-12': 'Ill Full Moon Poya Day ',
     '2019-12-11': 'Unduvap Full Moon Poya Day ',
     '2019-12-25': 'Christmas Day '}

slholidays.load_holidays(data)

allh = slholidays.get_all_holidays()
h=slholidays.get_next_holiday("2019-5-1",include_weekends=False)
r1 = slholidays.get_previous_holiday("2019-5-1",include_weekends=False)

hl = slholidays.holiday_name("2019-4-14")
h2 = slholidays.is_public_holiday("2019-5-1")
r2 = slholidays.number_of_days_to_next_holiday("2019-5-1",include_weekends=True)
r3 = slholidays.number_of_days_to_previous_holiday("2019-5-1",include_weekends=True)
d = slholidays.get_the_day("2019-04-14")
nm = slholidays.number_of_days_between("2019-01-15","2019-04-14",include_weekends=True)