import yaml
from google.cloud import bigquery
from google.oauth2 import service_account

#Add BQ Credentials
credentials = service_account.Credentials.from_service_account_file(
'C:\\Users\\pbelc\Documents\\Data_Test_Tool\\data_testing_tool\\secrets\\pb-data-tool-testing-67a4e3de6376.json')

#Define Project Details
project_id = 'pb-data-tool-testing'
client = bigquery.Client(credentials= credentials,project=project_id)

#Test to check for null values
def null_check(table, column, filter_condition=None):
   
    query = f"""
    SELECT COUNT(*) AS fail_count
    FROM `{table}`
    WHERE {column} IS NULL
    """
    if filter_condition:
        query = query + f" AND {filter_condition}"
        
    query_job = client.query(query)
    print(query)

    result = query_job.result().to_dataframe()

    #Create a view of the full query if wanting to pull all records
    full_check_query = query.replace( "COUNT(*) as fail_count", "*")

    return int(result['fail_count'][0]), full_check_query

#Test to check if 2 columns in a table are equal
def equality_check(table, column1, column2, filter_condition=None):
    query = f"""
    SELECT COUNT(*) AS fail_count
    FROM `{table}`
    WHERE {column1} != {column2}
    """
    if filter_condition:
        query = query + f" AND {filter_condition}"

    query_job = client.query(query)
    result = query_job.result().to_dataframe()

    #Create a view of the full query if wanting to pull all records
    full_check_query = query.replace( "COUNT(*) as fail_count", "*")

    return int(result['fail_count'][0]), full_check_query

#Test to check if a value in a column is negative
def negative_check(table, column1, filter_condition=None):
    query = f"""
    SELECT COUNT(*) AS fail_count
    FROM `{table}`
    WHERE {column1} < 0
    """
    if filter_condition:
        query = query + f" AND {filter_condition}"

    query_job = client.query(query)
    result = query_job.result().to_dataframe()

    #Create a view of the full query if wanting to pull all records
    full_check_query = query.replace( "COUNT(*) as fail_count", "*")

    return int(result['fail_count'][0]), full_check_query

#Test to check if a value in a column is 0
def zero_check(table, column1, filter_condition=None):
    query = f"""
    SELECT COUNT(*) AS fail_count
    FROM `{table}`
    WHERE {column1} = 0
    """
    if filter_condition:
        query = query + f" AND {filter_condition}"

    query_job = client.query(query)
    result = query_job.result().to_dataframe()

    #Create a view of the full query if wanting to pull all records
    full_check_query = query.replace( "COUNT(*) as fail_count", "*")

    return int(result['fail_count'][0]), full_check_query