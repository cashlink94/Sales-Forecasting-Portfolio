import pandas as pd
import numpy as np
import os

# Load dataset
df = pd.read_csv('data/raw/train.csv')

# Check the columns in the dataframe to confirm column names
print("Columns in dataset:", df.columns)

# Convert Date column to datetime type
df['Date'] = pd.to_datetime(df['Date'])

# Handle missing values
# Fill missing values for categorical columns with '0'
df['StateHoliday'].fillna('0', inplace=True)  # For categorical columns
df.fillna('0', inplace=True)  # For other columns that may contain strings

# Remove stores that were closed (Open == 0)
df = df[df['Open'] == 1]

# Feature engineering: Extract year, month, day, weekday from the Date column
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day
df['Weekday'] = df['Date'].dt.weekday  # Monday=0, Sunday=6

# Create lag feature for sales (previous day's sales)
df['Lag_Sales'] = df['Sales'].shift(1)

# Create rolling average for sales (7-day window)
df['Rolling_Avg_Sales'] = df['Sales'].rolling(window=7).mean()

# Drop any rows with missing values due to lag and rolling average
df.dropna(inplace=True)

# Ensure the 'processed' directory exists
os.makedirs('data/processed', exist_ok=True)

# Save the cleaned data to the processed folder
df.to_csv('data/processed/cleaned_sales_data.csv', index=False)

print("Data preprocessing completed successfully!")