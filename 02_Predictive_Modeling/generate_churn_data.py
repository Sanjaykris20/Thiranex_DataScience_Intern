import pandas as pd
import numpy as np
import os

os.makedirs("C:/Users/HP/Downloads/intern 4th sem/02_Predictive_Modeling", exist_ok=True)

np.random.seed(42)
n_samples = 1000

# Continuous variables
account_age = np.random.randint(1, 72, n_samples) # months
monthly_charges = np.random.uniform(20.0, 120.0, n_samples)
support_tickets = np.random.poisson(1.5, n_samples)

# Categorical variables
tech_support = np.random.choice([0, 1], n_samples, p=[0.6, 0.4])
device_protection = np.random.choice([0, 1], n_samples, p=[0.7, 0.3])
paperless_billing = np.random.choice([0, 1], n_samples, p=[0.3, 0.7])

# Logic for Churn probability (simulated ground truth)
# Churn increases with support tickets, monthly charges, and lower account age.
# Churn decreases if customer has tech support.
churn_logit = (
    0.05 * monthly_charges 
    + 0.8 * support_tickets 
    - 0.04 * account_age 
    - 1.2 * tech_support 
    - 0.5 * device_protection
    - 2.0  # intercept
)
churn_prob = 1 / (1 + np.exp(-churn_logit))
churn = np.random.binomial(1, churn_prob)

df = pd.DataFrame({
    'CustomerID': [f"CUST_{2000 + i}" for i in range(n_samples)],
    'Account_Age_Months': account_age,
    'Monthly_Charges': np.round(monthly_charges, 2),
    'Support_Tickets': support_tickets,
    'Tech_Support': tech_support,
    'Device_Protection': device_protection,
    'Paperless_Billing': paperless_billing,
    'Churn': churn
})

df.to_csv("C:/Users/HP/Downloads/intern 4th sem/02_Predictive_Modeling/customer_churn_data.csv", index=False)
print("Customer Churn dataset generated successfully!")
