import pandas as pd
import mplfinance as mpf
import os

def save_chart_image(df, filename):
    mpf.plot(df, type='candle', style='charles', volume=False,
             savefig=dict(fname=filename, dpi=100, bbox_inches='tight'))

def generate_images(csv_path, label, window_size=30, step=10):
    df = pd.read_csv(csv_path, parse_dates=['timestamp'])
    os.makedirs(f"images/{label}", exist_ok=True)
    for i in range(0, len(df) - window_size, step):
        chunk = df.iloc[i:i+window_size]
        chunk.set_index('timestamp', inplace=True)
        image_path = f"images/{label}/image_{i:04d}.png"
        save_chart_image(chunk, image_path)
    print(f"Generated candlestick images in images/{label}/")

if __name__ == "__main__":
    generate_images("data/raw_candles/BTCUSDT_15m.csv", label="uptrend")
