# Sales Forecasting Project

## Objective
Forecast daily sales using historical data to inform inventory and planning decisions.

## Data
- Historical sales data (2013–2015) in `data/cleaned_sales_data.csv`

## Methodology
- Python-based time series forecasting using ARIMA (2,1,2)
- 30-day forecast with confidence intervals
- Evaluation metrics calculated: RMSE, MAE, MAPE

## Scripts
- `train_model.py` → Fit ARIMA and generate forecast CSV
- `portfolio_plot.py` → Create clean forecast plot
- `portfolio_slide.py` → Combine plot + summary text
- `forecast_evaluation.py` → Compute forecast metrics
- `portfolio_slide_final.py` → Final portfolio-ready slide with plot, summary, and metrics

## Outputs
- `models/sales_forecast_arima.csv` → Forecasted sales
- `models/portfolio_slide_final.png` → Final portfolio-ready slide