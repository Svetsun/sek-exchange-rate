import json
import boto3
import urllib3
import datetime

# REPLACE WITH YOUR DATA FIREHOSE NAME
FIREHOSE_NAME = 'PUT-S3-KuAfV'

def lambda_handler(event, context):
    
    http = urllib3.PoolManager()
    
    r = http.request("GET", "https://v6.exchangerate-api.com/v6/1b6ed32781e96eed045de13b/latest/SEK")
    
    # turn it into a dictionary
    r_dict = json.loads(r.data.decode(encoding='utf-8', errors='strict'))
    
    
    
    
    # extract pieces of the dictionary
    processed_dict = {}
    processed_dict['time_last_update_utc'] = r_dict['time_last_update_utc']
    processed_dict['base_code'] = r_dict['base_code']
    processed_dict['EUR'] = r_dict['conversion_rates']['EUR']
    processed_dict['USD'] = r_dict['conversion_rates']['USD']
    processed_dict['DKK'] = r_dict['conversion_rates']['DKK']
    processed_dict['NOK'] = r_dict['conversion_rates']['NOK']
    processed_dict['time_now'] = str(datetime.datetime.now())
    
    
   
    
    
    # turn it into a string and add a newline
    msg = str(processed_dict) + '\n'
    
    fh = boto3.client('firehose')
    
    reply = fh.put_record(
        DeliveryStreamName=FIREHOSE_NAME,
        Record = {
                'Data': msg
                }
    )
    return reply