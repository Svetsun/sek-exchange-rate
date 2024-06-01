import json
import boto3
import urllib3
import datetime

# DATA FIREHOSE NAME
FIREHOSE_NAME = 'PUT-S3-QRMal'

# Initialize the Firehose client
firehose_client = boto3.client('firehose')

def lambda_handler(event, context):
    # Calculate the current system date
    end_date = datetime.date.today()
    
    # Calculate the first day of the previous month
    first_day_of_current_month = end_date.replace(day=1)
    start_date = (first_day_of_current_month - datetime.timedelta(days=1)).replace(day=1)
    
    delta = datetime.timedelta(days=1)

    current_date = start_date
    while current_date <= end_date:
        year_str = current_date.strftime("%Y")
        month_str = current_date.strftime("%m")
        day_str = current_date.strftime("%d")

        http = urllib3.PoolManager()

        try:
            # Properly format the URL with the date variables
            url = f"https://v6.exchangerate-api.com/v6/1b6ed32781e96eed045de13b/history/SEK/{year_str}/{month_str}/{day_str}"
            r = http.request("GET", url)
            
            # Check if the request was successful
            if r.status != 200:
                print(f"Error fetching data for {current_date}: Status {r.status}")
                current_date += delta
                continue
            # Turn it into a dictionary
            r_dict = json.loads(r.data.decode(encoding='utf-8', errors='strict'))
            
            # Extract pieces of the dictionary
            processed_dict = {
                'year': r_dict['year'],
                'month': r_dict['month'],
                'day': r_dict['day'],
                'base_code': r_dict['base_code'],
                'EUR': r_dict['conversion_rates']['EUR'],
                'USD': r_dict['conversion_rates']['USD'],
                'DKK': r_dict['conversion_rates']['DKK'],
                'NOK': r_dict['conversion_rates']['NOK'],
                'historical_timestamp': current_date.strftime("%Y-%m-%d")
            }
            
            # Turn it into a string and add a newline
            msg = json.dumps(processed_dict) + '\n'
            
            # Put record to Firehose
            reply = firehose_client.put_record(
                DeliveryStreamName=FIREHOSE_NAME,
                Record={'Data': msg}
            )
        except Exception as e:
            print(f"Exception occurred: {e}")
        
        current_date += delta

    return reply

            