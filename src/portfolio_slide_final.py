# src/portfolio_slide_final.py
from PIL import Image, ImageDraw, ImageFont

# Load plot
plot_path = 'models/sales_forecast_plot_YYYYMMDD_HHMMSS.png'
plot_img = Image.open(plot_path)
width, height = plot_img.size
canvas_height = height + 250
canvas = Image.new('RGB', (width, canvas_height), 'white')
canvas.paste(plot_img, (0,0))

draw = ImageDraw.Draw(canvas)
font_path = "arial.ttf"
try:
    font = ImageFont.truetype(font_path, 20)
except:
    font = ImageFont.load_default()

# Summary
summary_text = (
    "Project: Sales Forecasting with ARIMA Time Series Analysis\n"
    "Objective: Forecast daily sales for informed decision-making.\n"
    "Method: ARIMA(2,1,2) with 30-day forecast and confidence intervals.\n"
    "Outcome: Forecast vs Actual plot ready for portfolio."
)
metrics_text = (
    "Forecast Evaluation Metrics:\n"
    "RMSE: 3780.14\n"
    "MAE: 2440.62\n"
    "MAPE: 26.35%"
)

draw.multiline_text((10, height + 10), summary_text, fill='black', font=font, spacing=6)
draw.multiline_text((10, height + 130), metrics_text, fill='black', font=font, spacing=6)

final_slide_path = 'models/portfolio_slide_final.png'
canvas.save(final_slide_path, dpi=(300,300))
canvas.show()
print(f"Final portfolio slide saved: {final_slide_path}")