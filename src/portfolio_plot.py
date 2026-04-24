import pandas as pd
import matplotlib.pyplot as plt

# --- Load forecast CSV ---
forecast_csv_path = 'models/sales_forecast_arima_20260424_091648.csv'
forecast_df = pd.read_csv(forecast_csv_path, parse_dates=['Date'])

# --- Load historical sales CSV ---
historical_csv_path = 'data/processed/cleaned_sales_data.csv'
historical_df = pd.read_csv(historical_csv_path, parse_dates=['Date'])

# Sort by date just in case
historical_df = historical_df.sort_values('Date')
forecast_df = forecast_df.sort_values('Date')

# --- Plot ---
plt.figure(figsize=(12,6))

# Historical actual sales
plt.plot(historical_df['Date'], historical_df['Sales'], color='blue', label='Actual Sales', linewidth=2)

# Forecasted sales
plt.plot(forecast_df['Date'], forecast_df['Forecasted_Sales'], color='orange', label='Forecasted Sales', linewidth=2)

# Confidence interval shading
plt.fill_between(forecast_df['Date'], forecast_df['Lower_CI'], forecast_df['Upper_CI'], color='orange', alpha=0.2, label='Confidence Interval')

# Titles and labels
plt.title('Sales Forecast vs Actual Sales (ARIMA 2,1,2)', fontsize=16, weight='bold')
plt.xlabel('Date', fontsize=12)
plt.ylabel('Sales', fontsize=12)
plt.xticks(rotation=45)
plt.grid(alpha=0.3)
plt.legend()
plt.tight_layout()

# Save portfolio-ready plot
clean_plot_path = 'models/sales_forecast_portfolio.png'
plt.savefig(clean_plot_path, dpi=300)
plt.show()

print(f"Portfolio-ready plot saved: {clean_plot_path}")