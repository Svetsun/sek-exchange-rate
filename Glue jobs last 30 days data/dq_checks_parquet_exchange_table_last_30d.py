import sys
import awswrangler as wr

MY_DATABASE = 'exchange_data_svetlana'
PARQUET_TABLE_NAME = 'currency_exchange_table_parquet_last_30d'

# this check counts the number of NULL rows in the eur column
# if any rows are NULL, the check returns a number > 0
NULL_DQ_CHECK = f"""
SELECT 
    SUM(CASE WHEN eur IS NULL THEN 1 ELSE 0 END) AS res_col
FROM "{MY_DATABASE}"."{PARQUET_TABLE_NAME}"
;
"""

# run the quality check
df = wr.athena.read_sql_query(sql=NULL_DQ_CHECK, database="exchange_data_svetlana")

# exit if we get a result > 0
# else, the check was successful
if df['res_col'][0] > 0:
    sys.exit('Results returned. Quality check failed.')
else:
    print('Quality check passed.')