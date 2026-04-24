# src/forecast_evaluation.py
import pandas as pd
import numpy as np

# Load historical and forecast
historical_df = pd.read_csv('data/processed/cleaned_sales_data.csv', parse_dates=['Date']).sort_values('Date')
forecast_df = pd.read_csv('models/sales_forecast_arima_YYYYMMDD_HHMMSS.csv', parse_dates=['Date'])

# Align last 30 days of historical for evaluation
eval_historical = historical_df.tail(30).copy()
eval_forecast = forecast_df.head(30).copy()

errors = eval_historical['Sales'].values - eval_forecast['Forecasted_Sales'].values
rmse = np.sqrt(np.mean(errors**2))
mae = np.mean(np.abs(errors))
mape = np.mean(np.abs(errors / eval_historical['Sales'].values)) * 100

print("Forecast Evaluation Metrics:")
print(f"RMSE: {rmse:.2f}")
print(f"MAE: {mae:.2f}")
print(f"MAPE: {mape:.2f}%")