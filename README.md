#SEK Exchange Rate Data Ingestion and Visualization
Project Overview
This project is designed to ingest and process SEK exchange rate data using a variety of AWS services and visualize this data using Grafana Cloud. The data includes real-time rates, historical 30-day data, and 6-month data for SEK exchange rates. The primary purpose is to provide data for tasks such as price estimations in an e-commerce store.
Data Ingestion and Processing
Data Source
#The data is ingested from an exchange rate API which provides:

Real-time SEK exchange rates
30 days of historical exchange rate data
6 months of historical exchange rate data
AWS Cloud Services Used
AWS Lambda: A Python-based Lambda function is utilized to fetch data from the exchange rate API and trigger other AWS services.
Amazon Kinesis Data Firehose: This service is used to reliably load streaming data into data lakes, data stores, and analytics services.
Amazon S3: Data fetched by the Lambda function is stored in S3 buckets for durable, scalable storage.
AWS Glue: Glue is used to crawl the data stored in S3, cataloging it for further processing and creating ETL (Extract, Transform, Load) workflows.
AWS Athena: All data queries and analyses are performed using AWS Athena, allowing for efficient querying of data stored in S3.
Data Visualization
Grafana Cloud: Grafana Cloud is employed to visualize the processed data. This provides an interactive and user-friendly interface for monitoring and analyzing SEK exchange rate trends against EUR, USD, and DKK.
Workflow
Data Ingestion: The Lambda function periodically fetches real-time and historical data from the exchange rate API.
Data Streaming: Ingested data is streamed into Amazon Kinesis Data Firehose.
Data Storage: Data from Kinesis Data Firehose is stored in Amazon S3.
Data Crawling and Cataloging: AWS Glue crawls the data in S3 and catalogs it, preparing it for analysis.
Data Querying: Queries are performed using AWS Athena to analyze the data.
Data Visualization: Processed data is visualized in Grafana Cloud, allowing for real-time monitoring and historical analysis of SEK exchange rates.
Benefits
Real-Time and Historical Data: The project provides both real-time exchange rates and comprehensive historical data.
Scalable and Durable Storage: Using Amazon S3 ensures that data is stored reliably and can scale as needed.
Efficient Data Processing: AWS services like Lambda, Glue, and Athena provide a seamless and efficient workflow for data processing and analysis.
Interactive Visualizations: Grafana Cloud offers a powerful platform for visualizing data, making it easier to monitor trends and make informed decisions.
Versatile Data Usage: The data can be used for various tasks such as price estimations in an e-commerce store, statistics on a dashboard, and internal reporting spreadsheets.
This project leverages the power of AWS cloud services to provide a robust solution for monitoring and analyzing SEK exchange rates, with the added benefit of real-time visualization through Grafana Cloud.
