import pandas as pd
import numpy as np

# Seed for reproducibility
np.random.seed(42)

# Function to generate random product codes
def generate_product_code():
    return ''.join(np.random.choice(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'), size=4))

# Generate 100 rows of data with random values
product_ids = range(101, 201)
product_codes = [generate_product_code() for _ in range(100)]
prices_system_1 = np.round(np.random.uniform(5.99, 499.99, 100), 2)
prices_system_2 = prices_system_1.copy()  # Initially prices aligned

# Introduce some discrepancies and null values in system 2
for i in range(100):
    if np.random.rand() > 0.8:  # 20% chance of price discrepancy
        prices_system_2[i] = np.round(np.random.uniform(-105.99, 499.99), 2)
    if np.random.rand() > 0.9:  # 10% chance of null price in system 2
        prices_system_2[i] = np.nan
    if np.random.rand() > 0.95:  # 10% chance of 0 price in system 2
        prices_system_2[i] = 0

# Create random customer IDs
customer_ids = np.random.randint(1001, 2001, 100)

# Create a few missing records in each system
missing_in_system_1 = np.random.choice(product_ids, size=5, replace=False)
missing_in_system_2 = np.random.choice(product_ids, size=5, replace=False)

# Create system 1 and system 2 data
data_system_1 = {
    'system_1_PRODUCT_ID': [pid if pid not in missing_in_system_1 else None for pid in product_ids],
    'system_1_PRODUCT_CODE': [generate_product_code() for _ in range(100)],
    'system_1_PRODUCT_PRICE': prices_system_1,
    'system_1_CUSTOMER_ID': customer_ids
}

data_system_2 = {
    'system_2_PRODUCT_ID': [pid if pid not in missing_in_system_2 else None for pid in product_ids],
    'system_2_PRODUCT_CODE': [generate_product_code() for _ in range(100)],
    'system_2_PRODUCT_PRICE': prices_system_2,
    'system_2_CUSTOMER_ID': customer_ids
}

# Create DataFrames
df_system_1 = pd.DataFrame(data_system_1)
df_system_2 = pd.DataFrame(data_system_2)

# Merge the datasets on index
merged_df = pd.concat([df_system_1, df_system_2], axis=1)

# Display the first few rows of the merged DataFrame
#print(merged_df.head())

# If you want to save the DataFrame to a CSV file:
merged_df.to_csv("C:\\Users\\pbelc\\Documents\Data_Test_Tool\\data_testing_tool\\sample_test_dataset.csv", index=False)
