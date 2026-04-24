import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont

# --- Load the portfolio plot ---
plot_path = 'models/sales_forecast_portfolio.png'
plot_img = Image.open(plot_path)

# --- Create a white canvas larger than the plot for text ---
width, height = plot_img.size
canvas_height = height + 200  # extra space for text at bottom
canvas = Image.new('RGB', (width, canvas_height), 'white')

# --- Paste the plot onto the canvas ---
canvas.paste(plot_img, (0,0))

# --- Add text below the plot ---
draw = ImageDraw.Draw(canvas)
font_path = "arial.ttf"  # replace with a valid font path on your system
try:
    font = ImageFont.truetype(font_path, 20)
except:
    font = ImageFont.load_default()

summary_text = (
    "Project: Sales Forecasting with ARIMA Time Series Analysis\n"
    "Objective: Forecast daily sales for informed decision-making.\n"
    "Method: ARIMA(2,1,2) with 30-day forecast and confidence intervals.\n"
    "Outcome: Forecast vs Actual plot ready for portfolio."
)

# Draw text
margin = 10
draw.multiline_text((margin, height + 10), summary_text, fill='black', font=font, spacing=6)

# --- Save combined portfolio slide ---
combined_path = 'models/portfolio_slide.png'
canvas.save(combined_path, dpi=(300,300))
canvas.show()

print(f"Portfolio slide saved: {combined_path}")