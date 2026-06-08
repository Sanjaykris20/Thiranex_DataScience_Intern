import pandas as pd
import numpy as np
import json
import os
import matplotlib.pyplot as plt
import seaborn as sns

# Set style for visualizations
sns.set_theme(style="darkgrid")
plt.rcParams['figure.figsize'] = (10, 6)

print("Starting Data Cleaning Process...")

# 1. Load data
df_raw = pd.read_csv("C:/Users/HP/Downloads/intern 4th sem/01_Data_Cleaning_and_Visualization/raw_sales_data.csv")
print(f"Original shape: {df_raw.shape}")

# Create copy for cleaning
df = df_raw.copy()

# Record statistics for dashboard comparison
stats = {
    "original_rows": len(df_raw),
    "duplicate_rows_removed": 0,
    "missing_customer_ids": int(df_raw['Customer_ID'].isnull().sum()),
    "missing_dates": int(df_raw['Date'].isnull().sum()),
    "missing_purchase_amount": int(df_raw['Purchase_Amount'].isnull().sum()),
    "missing_customer_age": int(df_raw['Customer_Age'].isnull().sum()),
    "missing_payment_method": int(df_raw['Payment_Method'].isnull().sum()),
    "outliers_purchase_amount": int((df_raw['Purchase_Amount'] > 1000).sum() + (df_raw['Purchase_Amount'] < 0).sum()),
    "outliers_customer_age": int((df_raw['Customer_Age'] > 100).sum())
}

# 2. Handle duplicates
duplicates_count = df.duplicated().sum()
df = df.drop_duplicates()
stats["duplicate_rows_removed"] = int(duplicates_count)
print(f"Removed {duplicates_count} duplicate rows.")

# 3. Clean Customer_ID
# Fill missing customer IDs with a placeholder
df['Customer_ID'] = df['Customer_ID'].fillna('UNKNOWN')

# 4. Clean Date
# Standardize dates
df['Date'] = pd.to_datetime(df['Date'], errors='coerce', format='mixed')
# Impute missing dates by forward filling (since transactions are ordered)
df['Date'] = df['Date'].ffill().bfill()

# 5. Clean Product_Category
# Mapping for inconsistent categories
category_map = {
    'elec': 'Electronics',
    'electronics': 'Electronics',
    'ELECTRONICS': 'Electronics',
    'clothing': 'Clothing',
    'CLOTHING': 'Clothing',
    'home & kitchen': 'Home & Kitchen',
    'HOME & KITCHEN': 'Home & Kitchen',
    'home': 'Home & Kitchen',
    'HOME': 'Home & Kitchen',
    'books': 'Books',
    'BOOKS': 'Books',
    'beauty': 'Beauty',
    'BEAUTY': 'Beauty'
}
df['Product_Category'] = df['Product_Category'].replace(category_map)
df['Product_Category'] = df['Product_Category'].str.strip().str.title()
# Standardize spelling standard
df['Product_Category'] = df['Product_Category'].replace({'Elec': 'Electronics', 'Home': 'Home & Kitchen'})

# 6. Clean Purchase_Amount
# Remove negative values (turn to positive or impute)
df.loc[df['Purchase_Amount'] < 0, 'Purchase_Amount'] = np.nan
# Remove extreme outliers (> 1000)
df.loc[df['Purchase_Amount'] > 1000, 'Purchase_Amount'] = np.nan

# Impute missing purchase amounts with the median of their product category
category_medians = df.groupby('Product_Category')['Purchase_Amount'].median()
for cat in category_medians.index:
    df.loc[(df['Purchase_Amount'].isnull()) & (df['Product_Category'] == cat), 'Purchase_Amount'] = category_medians[cat]

# If any remaining (e.g. if category was null), fill with overall median
df['Purchase_Amount'] = df['Purchase_Amount'].fillna(df['Purchase_Amount'].median())

# 7. Clean Customer_Age
# Filter out unreasonable ages
df.loc[df['Customer_Age'] > 100, 'Customer_Age'] = np.nan
df.loc[df['Customer_Age'] < 0, 'Customer_Age'] = np.nan
# Impute missing ages with mean age (rounded)
mean_age = round(df['Customer_Age'].mean())
df['Customer_Age'] = df['Customer_Age'].fillna(mean_age).astype(int)

# 8. Clean Payment_Method
df['Payment_Method'] = df['Payment_Method'].fillna('Not Specified')

# Save clean CSV
df.to_csv("C:/Users/HP/Downloads/intern 4th sem/01_Data_Cleaning_and_Visualization/clean_sales_data.csv", index=False)
print(f"Cleaned shape: {df.shape}")

# Generate visualizations for output reports
plots_dir = "C:/Users/HP/Downloads/intern 4th sem/01_Data_Cleaning_and_Visualization/plots"
os.makedirs(plots_dir, exist_ok=True)

# 1. Product Category Sales Distribution
plt.figure()
sns.barplot(x='Product_Category', y='Purchase_Amount', data=df, estimator=sum, errorbar=None, palette='viridis')
plt.title('Total Revenue by Product Category')
plt.ylabel('Total Sales ($)')
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig(f"{plots_dir}/revenue_by_category.png")
plt.close()

# 2. Customer Age Distribution
plt.figure()
sns.histplot(df['Customer_Age'], bins=20, kde=True, color='skyblue')
plt.title('Customer Age Distribution')
plt.xlabel('Age')
plt.tight_layout()
plt.savefig(f"{plots_dir}/age_distribution.png")
plt.close()

# Save JavaScript data file for web dashboard
# Convert datetime back to string for JSON
df_dashboard = df.copy()
df_dashboard['Date'] = df_dashboard['Date'].dt.strftime('%Y-%m-%d %H:%M')
records = df_dashboard.to_dict(orient='records')

# Prepare summary statistics
summary_stats = {
    "total_revenue": float(df['Purchase_Amount'].sum()),
    "total_transactions": int(len(df)),
    "average_order_value": float(df['Purchase_Amount'].mean()),
    "unique_customers": int(df['Customer_ID'].nunique()),
    "category_revenue": df.groupby('Product_Category')['Purchase_Amount'].sum().to_dict(),
    "payment_distribution": df['Payment_Method'].value_counts().to_dict(),
    "cleaning_stats": stats
}

with open("C:/Users/HP/Downloads/intern 4th sem/01_Data_Cleaning_and_Visualization/dashboard_data.js", "w") as f:
    f.write(f"const salesData = {json.dumps(records)};\n")
    f.write(f"const summaryStats = {json.dumps(summary_stats)};\n")

print("Data cleaning completed. Plots and dashboard_data.js created!")
