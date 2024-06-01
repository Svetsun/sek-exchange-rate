import sys
import boto3

client = boto3.client('athena')

SOURCE_TABLE_NAME = 'currency_exchange_data_bucket_svetlana_1'
NEW_TABLE_NAME = 'currency_exchange_table_parquet_1'
NEW_TABLE_S3_BUCKET = 's3://currency-exchange-table-parquet-bucket/'
MY_DATABASE = 'exchange_data_svetlana'
QUERY_RESULTS_S3_BUCKET = 's3://athena-query-results-svetlana/'

# Refresh the table
queryStart = client.start_query_execution(
    QueryString = f"""
    CREATE TABLE {NEW_TABLE_NAME} WITH
    (external_location='{NEW_TABLE_S3_BUCKET}',
    format='PARQUET',
    write_compression='SNAPPY',
    partitioned_by = ARRAY['time_now'])
    AS

    SELECT
        time_last_update_utc
        ,base_code
        ,eur
        ,usd
        ,dkk
        ,nok
        ,time_now
       
        
        
    FROM "exchange_data_svetlana"."currency_exchange_data_bucket_svetlana_1"

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