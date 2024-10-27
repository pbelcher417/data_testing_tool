import yaml
from google.cloud import bigquery
from google.oauth2 import service_account
from datetime import date, datetime
from tests.define_tests import *

def load_config(config_file):
    with open(config_file, 'r') as file:
        return yaml.safe_load(file)    

def run_tests(config):
    test_results = []

    for table in config['tables']:
        table_name = table['name']
        for column in table['columns']:
            column_name = column['name']
            data_area = column['data_area']
            data_tested = column['data_tested']
            system = column['system']
            field_type = column['field_type']
            date_value_checked = column['date_value_checked']
            
            for test in column['tests']:
                print(test)
                business_rule = test['business_rule']  # Get custom test name
                test_type = test['type']  # Get test type
                print(test_type)
                
                if test_type == "is_null":
                    output = null_check(table_name, column_name)
                    failure_count = output[0]
                    full_query = output[1]

                elif test_type == "is_negative":
                    # Implement positive check
                    failure_count = negative_check(table_name, column_name)

                elif test_type == "column_equality":
                    target_column = test['target_column']
                    failure_count = equality_check(table_name, column_name, target_column)
                        
                test_results.append({
                    'data_area': data_area,
                    'data_tested': data_tested,
                    'system': system,
                    'field_type': field_type,
                    'date_value_checked': date_value_checked,
                    'business_rule': business_rule,
                    'table_name': table_name,
                    'column_name': column_name,
                    'failure_count': failure_count,
                    'full_query_ouput': full_query,
                    'test_date': date.today().strftime("%Y-%m-%d"),
                    'test_datetime': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        })

    return test_results

def load_to_bq(test_result_table, test_results):

    errors = client.insert_rows_json(test_result_table, test_results)

    if errors == []:
        print("Test Results loaded Successfully")

    else:
        print(f"Errors while inserting rows: {errors}")

if __name__ == "__main__":
    #Load Test configuaration file
    config = load_config('test_config.yml')

    #Run defined tests
    results = run_tests(config)

    table_name = 'pb-data-tool-testing.test_data.data_test_results'

    load_to_bq(table_name, results)



