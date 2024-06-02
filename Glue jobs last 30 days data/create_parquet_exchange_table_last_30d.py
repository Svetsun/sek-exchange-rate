import sys
import boto3

client = boto3.client('athena')

SOURCE_TABLE_NAME = 'new_previous_year_history_exchange_data_ingestion'
NEW_TABLE_NAME = 'currency_exchange_table_parquet_last_30d'
NEW_TABLE_S3_BUCKET = 's3://currency-exchange-bucket-parquet-last-30d/'
MY_DATABASE = 'exchange_data_svetlana'
QUERY_RESULTS_S3_BUCKET = 's3://athena-query-results-svetlana/'

# Refresh the table
queryStart = client.start_query_execution(
    QueryString = f"""
    CREATE TABLE {NEW_TABLE_NAME} WITH
    (external_location='{NEW_TABLE_S3_BUCKET}',
    format='PARQUET',
    write_compression='SNAPPY',
    partitioned_by = ARRAY['historical_timestamp'])
    AS

    SELECT
         base_code
        ,eur
        ,usd
        ,dkk
        ,nok
        ,historical_timestamp
       
        
        
    FROM "{MY_DATABASE}"."{SOURCE_TABLE_NAME}"

    ;
    """,
    QueryExecutionContext = {
        'Database': f'{MY_DATABASE}'
    }, 
    ResultConfiguration = { 'OutputLocation': f'{QUERY_RESULTS_S3_BUCKET}'}
)
# list of responses
resp = ["FAILED", "SUCCEEDED", "CANCELLED"]

# get the response
response = client.get_query_execution(QueryExecutionId=queryStart["QueryExecutionId"])

# wait until query finishes
while response["QueryExecution"]["Status"]["State"] not in resp:
    response = client.get_query_execution(QueryExecutionId=queryStart["QueryExecutionId"])
    
# if it fails, exit and give the Athena error message in the logs
if response["QueryExecution"]["Status"]["State"] == 'FAILED':
    sys.exit(response["QueryExecution"]["Status"]["StateChangeReason"])