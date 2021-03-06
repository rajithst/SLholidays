# -*- coding: utf-8 -*-
import csv
from os.path import join,dirname
    
def load_sl_public_holidays():
    module_path = dirname('__file__')
    with open('slholidays/data/public_holidays.csv') as csv_file:
        csv_reader = csv.reader(csv_file,delimiter=',')
        line_counter = 0
        hol_names = []
        hol_dates = []
        for row in csv_reader:
            if line_counter!=0:
                hol_names.append(row[0])
                hol_dates.append(row[2])
            line_counter+=1
    
        return dict(zip(hol_dates,hol_names))
    
