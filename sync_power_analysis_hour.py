#!/usr/bin/env python3
import power_analysis_hour
import json
from datetime import datetime
from datetime import timedelta

import time
import timeit
from timeit import default_timer as timer




pah = power_analysis_hour

def main():
 
    start_date = datetime.now() - timedelta(days=30)
    input = {
    "energyhubid": "78:a5:04:ff:40:bb",
    "starttime": datetime(2016,10,1,0,0,0),
    "endtime": datetime(2016,10,1,23,0,0),#datetime.now() ,
    "userid": "testuser",
    "resultsid":"a1",
    "analysismodel":"HOURLYPOWER",
    }
    #print("\nRun the  aggregation for the input\n")
    #print(input)
    #print("\nGet aggregate for the input\n")
    start1 = timer()
    start2 = time.perf_counter()
    print(start1)
    print(start2)
    aggr_data = pah.mdb_get_energy_counter_data_grouped_hourly(input) #pah.mdb_test(input) #
    print(len(aggr_data))
    #print(len(pah.mdb_test(input)))
    end1 = timer()
    end2 = time.perf_counter()
    print(end1)
    print(end2)
    print('mdb_get_energy_counter_data_grouped {0} {1}'.format(end1 - start1,end2-start2))   
    with open(datetime.now().strftime("%Y_%m_%d_")+"perftest.txt", "a") as myfile:
        myfile.write('mdb_get_energy_counter_data_grouped, {0}, {1}\n'.format(end1 - start1,end2-start2))
    #print(aggr_data)
    #print("\nCalculate average and format\n")
    start1 = timer()
    start2 = time.perf_counter()
    print(start1)
    print(start2)    
    hub_aggr = pah.get_energy_counter_aggregate(aggr_data)
    end1 = timer()
    end2 = time.perf_counter()
    print(end1)
    print(end2)
    print('get_energy_counter_aggregate, {0}, {1}\n'.format(end1 - start1,end2-start2))   
    input["data"]=list(hub_aggr)
    print(input)
    start1 = timer()
    start2 = time.perf_counter()
    print(start1)
    print(start2)    

    #pah.mdb_setup_poweranalysishour_job_collection()
    # pad.mdb_setup_poweranalysisday_job_collection()

if __name__ == "__main__":
    # execute only if run as a script
    main()
	
	






