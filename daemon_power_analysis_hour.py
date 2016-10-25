#!/usr/bin/env python3
import power_analysis_hour
import json
import re, time
import pymongo
pah = power_analysis_hour
while True:
    cursor = pah.mdb_get_cursor()
    while cursor.alive:
        try:
            doc = cursor.next()
            print("Found")
            print(doc)
            # New job found
            aggr_data = pah.mdb_get_energy_counter_data_grouped_hourly(doc)
            print(len(aggr_data))
            hub_aggr = pah.get_energy_counter_aggregate(aggr_data)
            doc["data"]=list(hub_aggr)
            pah.mdb_insert_poweranalysishour_result(doc)
            pah.mdb_mark_job_done(doc)
        # do_something(msg)
        except StopIteration:
            print("Out")
            time.sleep(2)