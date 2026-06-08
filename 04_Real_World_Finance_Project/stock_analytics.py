import pandas as pd
import numpy as np
import json
import os
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load stock prices
df = pd.read_csv("C:/Users/HP/Downloads/intern 4th sem/04_Real_World_Finance_Project/stock_prices.csv")
df['Date'] = pd.to_datetime(df['Date'])

stocks = ['TechCorp', 'EcoEnergy', 'MedHealth']
results = {}

# Risk-free rate (annualized, mapped to daily)
rf_daily = 0.02 / 252

# Output prediction days
n_forecast = 10

for stock in stocks:
    # 1. Moving Averages
    df[f'{stock}_SMA20'] = df[stock].rolling(window=20).mean()
    df[f'{stock}_SMA50'] = df[stock].rolling(window=50).mean()
    
    # 2. Returns
    daily_returns = df[stock].pct_change().dropna()
    cumulative_returns = (1 + daily_returns).cumprod() - 1
    
    # 3. Metrics
    mean_return = daily_returns.mean()
    volatility = daily_returns.std()
    
    # Annualized metrics
    ann_return = mean_return * 252
    ann_vol = volatility * np.sqrt(252)
    sharpe = (ann_return - 0.02) / ann_vol if ann_vol > 0 else 0.0
    
    # 4. Simple Linear Forecasting for next 10 days
    X_trend = np.arange(len(df)).reshape(-1, 1)
    y_trend = df[stock].values
    model = LinearRegression()
    model.fit(X_trend, y_trend)
    
    # Forecast future values
    future_X = np.arange(len(df), len(df) + n_forecast).reshape(-1, 1)
    forecast_vals = model.predict(future_X)
    
    # If the trend goes down too fast, floor at 10.0
    forecast_vals = np.clip(forecast_vals, 10.0, None).tolist()
    
    results[stock] = {
        "current_price": float(df[stock].iloc[-1]),
        "annualized_return": float(ann_return),
        "volatility": float(ann_vol),
        "sharpe_ratio": float(sharpe),
        "sma20": df[f'{stock}_SMA20'].fillna(df[stock]).tolist(),
        "sma50": df[f'{stock}_SMA50'].fillna(df[stock]).tolist(),
        "forecast": forecast_vals
    }

# Save output plots
plots_dir = "C:/Users/HP/Downloads/intern 4th sem/04_Real_World_Finance_Project/plots"
os.makedirs(plots_dir, exist_ok=True)

plt.figure(figsize=(12, 6))
for stock in stocks:
    plt.plot(df['Date'], df[stock], label=stock)
plt.title('Stock Performance History')
plt.xlabel('Date')
plt.ylabel('Price ($)')
plt.legend()
plt.tight_layout()
plt.savefig(f"{plots_dir}/stock_history.png")
plt.close()

# Prepare timeline for UI
dates_list = df['Date'].dt.strftime('%Y-%m-%d').tolist()

# Add forecast dates
last_date = df['Date'].iloc[-1]
forecast_dates = [(last_date + pd.Timedelta(days=i*1.4)).strftime('%Y-%m-%d') for i in range(1, n_forecast + 1)]

export_data = {
    "dates": dates_list,
    "forecast_dates": forecast_dates,
    "stocks": {s: df[s].tolist() for s in stocks},
    "metrics": results
}

with open("C:/Users/HP/Downloads/intern 4th sem/04_Real_World_Finance_Project/finance_data.js", "w") as f:
    f.write(f"const financeResults = {json.dumps(export_data)};\n")

print("Financial modeling and stock forecasts completed. finance_data.js generated!")
