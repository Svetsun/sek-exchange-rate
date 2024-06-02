# SEK Exchange Rate Data Ingestion and Visualization
---
## Project Overview
This project is designed to ingest and process SEK exchange rate data using a variety of AWS services and visualize this data using Grafana Cloud. The data includes real-time rates, historical 30-day data, and 6-month data for SEK exchange rates. The primary purpose is to provide data for tasks such as price estimations in an e-commerce store.
## Questions this Project Seeks to Answer
1. What are the current SEK exchange rates against EUR, USD, and DKK in real-time?
2. How have the SEK exchange rates fluctuated over the past 30 days?
3. What are the trends in SEK exchange rates over the past 6 months?
4. How can SEK exchange rate data be used for accurate price estimations in an e-commerce store?
## Data Ingestion and Processing
### Data Source
The data is ingested from two different [Exchange rate API](https://www.exchangerate-api.com/),

which provides:

- Real-time SEK exchange rates,

- Last 30 days of historical exchange rate data,

- Last 6 months of historical exchange rate data.

Real time data set is updated automatically by Glue workflow, hourly. Last 30 days and Last 6 months data set is updated automatically by Glue workflow, daily. 

### AWS Cloud Services Used
`AWS Lambda`: A Python-based Lambda function is utilized to fetch data from the exchange rate API and trigger other AWS services.

`Amazon Kinesis Data Firehose`: This service is used to reliably load streaming data into data lakes, data stores, and analytics services.

`Amazon S3`: Data fetched by the Lambda function is stored in S3 buckets for durable, scalable storage.

`AWS Glue`: Glue is used to crawl the data stored in S3, cataloging it for further processing and creating ETL (Extract, Transform, Load) workflows.

`AWS Athena`: All data queries and analyses are performed using AWS Athena, allowing for efficient querying of data stored in S3.

## Data Visualization

### Grafana Cloud:
Grafana Cloud is employed to visualize the processed data. This provides an interactive and user-friendly interface for monitoring and analyzing SEK exchange rate trends against EUR, USD, and DKK.

---

#### Real-time and 30 days of historical exchange rate data:

<img width="803" alt="Grafana dashboard real time" src="https://github.com/Svetsun/sek-exchange-rate/assets/124575095/198d0591-42ae-4d94-8f53-8597731b83cf">

#### 6 months of historical exchange rate data

<img width="804" alt="Grafana dashboard historical data" src="https://github.com/Svetsun/sek-exchange-rate/assets/124575095/3cd862a1-ff32-49e4-94f5-15f5230a92f9">


### Dashboards you can see here:

- [Real-time SEK exchange rates](https://feasun.grafana.net/dashboard/snapshot/Y4g6VzPeNJBJm5ZD0bpnQrA2u9IWKvtI)

- [30 days of historical exchange rate data](https://feasun.grafana.net/dashboard/snapshot/NEnRSuvHGq8dUlY0xKdVHnGEm0Ls1qZG)

- [6 months of historical exchange rate data](https://feasun.grafana.net/dashboard/snapshot/AvRL4yKnAXYGDWGL1o8wiDXRnI8enSLE)

  
## Workflow
- Data Ingestion: The Lambda function periodically fetches real-time and historical data from the exchange rate API.

- Data Streaming: Ingested data is streamed into Amazon Kinesis Data Firehose.

- Data Storage: Data from Kinesis Data Firehose is stored in Amazon S3.

- Data Crawling, Cataloging and Glue workflow: AWS Glue crawls the data in S3 and catalogs it, preparing it for analysis by automating Glue workflow.

<img width="770" alt="Currency exchange real time Glue workflow" src="https://github.com/Svetsun/sek-exchange-rate/assets/124575095/8ea6e3b4-4214-4955-b64c-4627a7451dfb">

On diagram: Glue workflow for Real time currency exchange data processing


- Data Querying: Queries are performed using AWS Athena to analyze the data.

- Data Visualization: Processed data is visualized in Grafana Cloud, allowing for real-time monitoring and historical analysis of SEK exchange rates.

Hourly and daily updates are performed using EventBridge Schedule to activate Lambda functions and by scheduling Glue data workflow executions.

## Benefits
- Real-Time and Historical Data: The project provides both real-time exchange rates and comprehensive historical data.

- Scalable and Durable Storage: Using Amazon S3 ensures that data is stored reliably and can scale as needed.
- Efficient Data Processing: AWS services like Lambda, Glue, and Athena provide a seamless and efficient workflow for data processing and analysis.
- Interactive Visualizations: Grafana Cloud offers a powerful platform for visualizing data, making it easier to monitor trends and make informed decisions.
- Versatile Data Usage: The data can be used for various tasks such as price estimations in an e-commerce store, statistics on a dashboard, and internal reporting spreadsheets.
- This project leverages the power of AWS cloud services to provide a robust solution for monitoring and analyzing SEK exchange rates, with the added benefit of real-time visualization through Grafana Cloud.
- 
## Project Deployment Description

### Overview
The deployment of this project involves setting up the infrastructure on AWS to ingest, process, store, and visualize SEK exchange rate data. The deployment process includes configuring AWS services, setting up automation for data updates, and ensuring the integration with Grafana Cloud for visualization.

#### Steps for Deployment
1. Set Up AWS Services

- `Amazon S3`: Create S3 buckets to store raw and processed data.

- `AWS Lambda´: Deploy Python-based Lambda functions to fetch real-time and historical exchange rate data from the API.

- `Amazon Kinesis Data Firehose`: Configure Kinesis Data Firehose to stream data from Lambda functions to S3.

- `AWS Glue´: Set up Glue crawlers to catalog the data stored in S3 and create Glue ETL workflows.

- `AWS Athena`: Configure Athena to query the data cataloged by Glue.

2. Configure EventBridge

- Set up `EventBridge schedules` to trigger Lambda functions for hourly and daily data updates.
 
- Schedule  `Glue ETL` data workflow executions to ensure timely processing and storage of data.
3. Data Ingestion and Processing

- Implement `Lambda` function you need. Ensure Lambda functions are correctly fetching data from the exchange rate API and streaming it to Kinesis Data Firehose.
 
- Verify that Glue crawlers are cataloging data and Glue ETL workflows are running as scheduled.
  
4. Visualization with Grafana Cloud

- Set up `Grafana Cloud` and configure data sources to pull data from `AWS Athena`.
  
- Create dashboards in Grafana to visualize real-time and/or historical SEK exchange rate data against EUR, USD, and DKK.

## Future Improvements

- Cost Optimization: Analyze and optimize the AWS services used to reduce operational costs while maintaining performance and reliability.

- Data Quality Monitoring: Develop mechanisms to continuously monitor the quality and accuracy of the ingested data, ensuring reliability.
