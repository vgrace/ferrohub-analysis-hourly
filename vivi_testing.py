import pymongo
import power_analysis_hour
from datetime import datetime
from random import randint

pah = power_analysis_hour
#client = pymongo.MongoClient("localhost", 27017)
#db = client.test


def main():


	job = {
	    "energyhubid": "78:a5:04:ff:40:bb",
	    "starttime": datetime(2016,10,1,4,0,0),
	    "endtime": datetime(2016,10,1,8,0,0),
	    "userid": "testuser",
	    "resultsid":"ABCD" + str(randint(0,1000)),
	    "analysismodel":"HOURLYPOWER",
	    "jobstatus":0
	}; 

	#pah.mdb_insert_poweranalysishour_job(job)
	## ORG
	##aggr_data = pah.mdb_get_energy_counter_data_grouped_hourly(job)
	##print(len(aggr_data))
	##hub_aggr = pah.get_energy_counter_aggregate(aggr_data)

	## NEW
	data = pah.mdb_get_energy_counter_data_new_hourly(job)
	hub_aggr = pah.get_energy_counter_aggregate_new(data)
	##print(data)
	print(list(hub_aggr))

	
#print(db.poweranalysishour_jobs.insert_one(job).inserted_id)


#print(db.name)
#print(db.test_poweranalysisday_jobs)
#print(db.test_poweranalysisday_jobs.insert_one({"x": 8}).inserted_id)
#print(db.test_poweranalysisday_jobs.find_one())

#date = "2016-10-18 00:00:00"
#datestr = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
#print(datestr)
#date2 = "2016-10-18 23:00:00"
#date2str = datetime.strptime(date2, "%Y-%m-%d %H:%M:%S")
#print(date2str)
#print("Hello you handsome devil!")

if __name__ == "__main__":
    # execute only if run as a script
    main()