# src/train_model.py
import pandas as pd
import matplotlib.pyplot as plt
import os
from statsmodels.tsa.arima.model import ARIMA
from datetime import datetime

# --- Load cleaned sales data ---
df = pd.read_csv('data/processed/cleaned_sales_data.csv', parse_dates=['Date'])
df = df.dropna(subset=['Sales'])
df = df[df['Sales'] >= 0]
df = df.sort_values('Date')
df.set_index('Date', inplace=True)

# --- Optional: fill missing dates if needed ---
# df = df.asfreq('D')
# df['Sales'].fillna(method='ffill', inplace=True)

# --- Fit ARIMA model ---
arima_order = (2,1,2)
model = ARIMA(df['Sales'], order=arima_order)
fitted_model = model.fit()

# --- Forecast next 30 days ---
forecast_steps = 30
forecast_result = fitted_model.get_forecast(steps=forecast_steps)
forecast_values = forecast_result.predicted_mean
conf_int = forecast_result.conf_int()

# --- Generate forecast dates ---
last_date = df.index[-1]
forecast_dates = pd.date_range(last_date + pd.Timedelta(days=1), periods=forecast_steps, freq='D')

# --- Save forecast CSV ---
os.makedirs('models', exist_ok=True)
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
forecast_df = pd.DataFrame({
    'Date': forecast_dates,
    'Forecasted_Sales': forecast_values,
    'Lower_CI': conf_int.iloc[:,0],
    'Upper_CI': conf_int.iloc[:,1]
})
forecast_csv_path = f'models/sales_forecast_arima_{timestamp}.csv'
forecast_df.to_csv(forecast_csv_path, index=False)

# --- Plot actual vs forecast ---
plt.figure(figsize=(12,6))
plt.plot(df.index, df['Sales'], color='blue', label='Actual Sales', linewidth=2)
plt.plot(forecast_dates, forecast_values, color='orange', label='Forecasted Sales', linewidth=2)
plt.fill_between(forecast_dates, conf_int.iloc[:,0], conf_int.iloc[:,1], color='orange', alpha=0.2)
plt.title(f'Sales Forecast vs Actual (ARIMA{arima_order})', fontsize=16, weight='bold')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()

forecast_plot_path = f'models/sales_forecast_plot_{timestamp}.png'
plt.savefig(forecast_plot_path, dpi=300)
plt.close()

print(f"Forecast CSV saved: {forecast_csv_path}")
print(f"Forecast plot saved: {forecast_plot_path}")