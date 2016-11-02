#!/usr/bin/env python3
import power_analysis_hour
import json
from datetime import datetime
from datetime import timedelta

pah = power_analysis_hour

def main():
    #pah.mdb_setup_poweranalysishour_job_collection()
    pah.mdb_setup_poweranalysishour_jobs_results_collection()

if __name__ == "__main__":
    # execute only if run as a script
    main()
	
	






