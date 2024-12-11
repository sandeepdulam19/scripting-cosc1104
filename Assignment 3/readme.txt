Cloud-Based Data Transformation Pipeline

"PRE-REQUISITES and Steps of execution"

- login into GCP account
- enable "Cloud Storage API" and "BigQuery API"
- create service account, download the key and set environment variables path in local machine.


- create a bucket and upload the dataset i.e.,CSV/JSON file into it.
- In BigQuery create a dataset and a table


- In python code replace with your own credentials.

BUCKET_NAME = 'sandeep-bucket' 		  # bucket name
SOURCE_FILE_PATH = 'assignment/data.csv'  # Path in GCS bucket
DESTINATION_DATASET = 'scripting' 	  # big query dataset name
DESTINATION_TABLE = 'sandeep' 		  # big query table name



- navigate to the location where python code file is present
- connect the local machine to GCP in Command line
- run python script


- the code executes and the output data is stored in "BigQuery Table"

- attached a sample dataset for running the code.