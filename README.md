# Data Testing Tool

## Purpose
This is a simple tool for data quality testing in Bigquery. 
Tests are defined via YAML configuration, SQL is then generated based on the provided dataset and column names, and run directly on Bigquery.
The configuration file allows additional information to be stored against each test highlighting the area of the test, what is being tested etc.

In general I would recommend building tests in to your transformation logic using DBT or Terraform.
However, this project was unable to use these tools, so this custom framework was created.

## Adding additional tests
To add any additional tests, create the test function in define_tests.py.
Test functions return both the number of failures for the given test, as well as the SQL required to get the full results of any failures.

You will also need to update the run_tests.py file to run the newly defined tests.

Once created, you can now add to the config YAML file to run the associated tests.