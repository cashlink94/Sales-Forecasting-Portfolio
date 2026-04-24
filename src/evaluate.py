from sklearn.metrics import mean_absolute_error, mean_squared_error
import pandas as pd
import numpy as np

# Load actual sales data and predicted sales data
df_actual = pd.read_csv('data/processed/cleaned_sales_data.csv')
forecast = pd.read_csv('models/sales_forecast.csv')

# Calculate MAE and RMSE
mae = mean_absolute_error(df_actual['Sales'], forecast['yhat'][:len(df_actual)])
rmse = np.sqrt(mean_squared_error(df_actual['Sales'], forecast['yhat'][:len(df_actual)]))

print(f'Mean Absolute Error (MAE): {mae}')
print(f'Root Mean Squared Error (RMSE): {rmse}')