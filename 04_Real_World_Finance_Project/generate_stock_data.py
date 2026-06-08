import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

os.makedirs("C:/Users/HP/Downloads/intern 4th sem/04_Real_World_Finance_Project", exist_ok=True)

np.random.seed(42)
n_days = 180

# Date range
end_date = datetime.today()
start_date = end_date - timedelta(days=n_days * 1.4) # account for weekends roughly
date_range = pd.date_range(end=end_date, periods=n_days, freq='B') # Business days

# Generate prices with geometric brownian motion or similar trends
def generate_stock_prices(start_price, drift, volatility, n):
    returns = np.random.normal(drift / 252, volatility / np.sqrt(252), n)
    price_path = start_price * np.exp(np.cumsum(returns))
    return np.round(price_path, 2)

# Generate three stocks
tech_prices = generate_stock_prices(start_price=150.0, drift=0.15, volatility=0.22, n=n_days) # High return, mid risk
green_prices = generate_stock_prices(start_price=80.0, drift=0.08, volatility=0.35, n=n_days) # Volatile, lower return
health_prices = generate_stock_prices(start_price=120.0, drift=0.05, volatility=0.12, n=n_days) # Steady growth, low risk

df = pd.DataFrame({
    'Date': date_range.strftime('%Y-%m-%d'),
    'TechCorp': tech_prices,
    'EcoEnergy': green_prices,
    'MedHealth': health_prices
})

df.to_csv("C:/Users/HP/Downloads/intern 4th sem/04_Real_World_Finance_Project/stock_prices.csv", index=False)
print("Historical Stock Prices dataset generated successfully!")
