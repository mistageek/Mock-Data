#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 20:33:37 2020

@author: mistageek
"""
import numpy as np
import calendar
import random
import datetime

def gen_date(month):
    # Generate date and time in the format mm/dd/year H:m:s
    day_range = calendar.monthrange(2020, month)[1]
    random_day = random.randint(1, day_range)
    
    if random.random() < 0.5:
        date = datetime.datetime(2020, month, random_day, 12, 0, 0)
    else:
        date = datetime.datetime(2020, month, random_day, 20, 0,0)
    
    time_offset = np.random.normal(loc=0, scale=10800)
    final_date = date + datetime.timedelta(seconds=time_offset)

    return final_date.strftime("%m/%d/%y %H:%M:%S")