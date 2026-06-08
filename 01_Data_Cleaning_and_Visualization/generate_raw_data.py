import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

# Create directory if it doesn't exist
os.makedirs("C:/Users/HP/Downloads/intern 4th sem/01_Data_Cleaning_and_Visualization", exist_ok=True)

np.random.seed(42)
n_rows = 1200

# Generate columns
transaction_ids = [f"TXN_{1000 + i}" for i in range(n_rows)]
customer_ids = [f"CUST_{np.random.randint(100, 300)}" for _ in range(n_rows)]
# Add some missing customer IDs
for i in np.random.choice(range(n_rows), 50, replace=False):
    customer_ids[i] = None

# Dates with different formats and some nulls
base_date = datetime(2026, 1, 1)
dates = []
for i in range(n_rows):
    dt = base_date + timedelta(days=int(np.random.randint(0, 150)), hours=int(np.random.randint(0, 24)))
    if i % 15 == 0:
        dates.append(dt.strftime("%d-%m-%Y %H:%M"))
    elif i % 20 == 0:
        dates.append(None)
    else:
        dates.append(dt.strftime("%Y-%m-%d %H:%M:%S"))

# Product Categories with typos and inconsistencies
categories = ['Electronics', 'Clothing', 'Home & Kitchen', 'Books', 'Beauty']
category_choices = []
for _ in range(n_rows):
    choice = np.random.choice(categories)
    # Introduce typos/inconsistencies
    r = np.random.rand()
    if r < 0.05:
        choice = choice.upper()
    elif r < 0.10:
        choice = choice.lower()
    elif r < 0.12:
        if choice == 'Electronics': choice = 'Elec'
        elif choice == 'Home & Kitchen': choice = 'Home'
    category_choices.append(choice)

# Purchase Amount with outliers and negatives
purchase_amounts = np.random.normal(120, 80, n_rows).tolist()
# Add extreme outliers and negative values
for i in np.random.choice(range(n_rows), 25, replace=False):
    purchase_amounts[i] = 9999.99  # Extreme positive outlier
for i in np.random.choice(range(n_rows), 15, replace=False):
    purchase_amounts[i] = -50.0  # Negative outlier
for i in np.random.choice(range(n_rows), 30, replace=False):
    purchase_amounts[i] = None  # Missing values

# Customer age with missing values and outliers
ages = np.random.randint(18, 70, n_rows).astype(float).tolist()
for i in np.random.choice(range(n_rows), 80, replace=False):
    ages[i] = None
for i in np.random.choice(range(n_rows), 10, replace=False):
    ages[i] = 150.0  # Outlier age

# Payment method with missing values
payment_methods = np.random.choice(['Credit Card', 'PayPal', 'Debit Card', 'Cash'], n_rows).tolist()
for i in np.random.choice(range(n_rows), 60, replace=False):
    payment_methods[i] = None

# Create DataFrame
df = pd.DataFrame({
    'Transaction_ID': transaction_ids,
    'Customer_ID': customer_ids,
    'Date': dates,
    'Product_Category': category_choices,
    'Purchase_Amount': purchase_amounts,
    'Customer_Age': ages,
    'Payment_Method': payment_methods
})

# Add duplicates
duplicates = df.sample(n=50, random_state=42)
df = pd.concat([df, duplicates], ignore_index=True)

# Shuffle
df = df.sample(frac=1, random_state=101).reset_index(drop=True)

# Save raw dataset
df.to_csv("C:/Users/HP/Downloads/intern 4th sem/01_Data_Cleaning_and_Visualization/raw_sales_data.csv", index=False)
print("Raw dirty dataset generated successfully!")
