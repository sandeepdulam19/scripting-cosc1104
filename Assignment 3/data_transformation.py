# Author - Sandeep Dulam
# Date - 10 Dec 2024
# sandeep dulam git link - https://github.com/sandeepdulam19/scripting-cosc1104

'''
python script for automating the transformation of data in cloud storage before it is loaded into analytics tools

'''

import pandas as pd
from google.cloud import storage, bigquery
from io import StringIO

# initializing google cloud clients
storage_client = storage.Client()
bigquery_client = bigquery.Client()

# constants
BUCKET_NAME = 'sandeep-bucket'
SOURCE_FILE_PATH = 'assignment/data.csv'  # path in GCS bucket
DESTINATION_DATASET = 'scripting'
DESTINATION_TABLE = 'sandeep'


# function to download the file from google cloud storage and return it as a pandas dataframe
def download_data_from_gcs(bucket_name, file_path):
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(file_path)
    content = blob.download_as_text()  
    
    try:
        data = pd.read_csv(StringIO(content))
    except Exception as e:
        print(f"Error reading CSV: {e}")
        raise e
    
    return data


# function to perform dynamic data cleaning and transformation
def clean_and_transform_data(data):
    
    # remove rows with missing values
    data = data.dropna()

    # to make sure all column names are lowercase
    data.columns = [col.lower() for col in data.columns]

    # simple aggregation sum values for each category
    if 'category' in data.columns and 'value' in data.columns:
        data_agg = data.groupby('category')['value'].sum().reset_index()
        return data_agg
    
    return data


# function to load the transformed data into google bigquery
def load_data_to_bigquery(data, dataset_name, table_name):
    # convert the pandas DataFrame to a CSV string to upload
    csv_data = data.to_csv(index=False)
    
    # BigQuery dataset and table references
    dataset_ref = bigquery_client.dataset(dataset_name)
    table_ref = dataset_ref.table(table_name)
    
    # defining job configuration with autodetection for schema
    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV,  
        write_disposition=bigquery.WriteDisposition.WRITE_APPEND,  
        autodetect=True  
    )

    # Uploading to BigQuery
    load_job = bigquery_client.load_table_from_file(
        StringIO(csv_data), table_ref, job_config=job_config
    )

    load_job.result() 

    print(f"Data successfully loaded into BigQuery table {table_name}.")



# main function
def main():
    data = download_data_from_gcs(BUCKET_NAME, SOURCE_FILE_PATH)
    
    # cleaning and transforming the data
    transformed_data = clean_and_transform_data(data)
    
    # loading the transformed data into BigQuery
    load_data_to_bigquery(transformed_data, DESTINATION_DATASET, DESTINATION_TABLE)


if __name__ == '__main__':
    main()
