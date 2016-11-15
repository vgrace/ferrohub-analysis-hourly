#!/usr/bin/env python3
from datetime import datetime
from datetime import date
from datetime import timedelta
from datetime import time

# Constants
no_of_seconds_in_a_day = 24 * 60 *60
cest_offset_ms = 1000 * 60 * 60 * 1 # Two hours in milliseconds

def round_down_datetime(datetime_value):
    return datetime.combine(datetime_value,time.min)

def round_up_datetime(datetime_value):
    return datetime.combine(datetime_value,time.max)
	
def cest_as_utc(datetime_value):
     return datetime_value- timedelta(milliseconds=cest_offset_ms)