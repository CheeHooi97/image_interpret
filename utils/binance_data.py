import requests
import pandas as pd
import os

def get_binance_klines(symbol="BTCUSDT", interval="15m", limit=500):
    url = "https://api.binance.com/api/v3/klines"
    params = {"symbol": symbol, "interval": interval, "limit": limit}
    response = requests.get(url, params=params)
    data = response.json()

    df = pd.DataFrame(data, columns=[
        'timestamp', 'open', 'high', 'low', 'close', 'volume',
        '_1', '_2', '_3', '_4', '_5', '_6'
    ])
    df = df[['timestamp', 'open', 'high', 'low', 'close', 'volume']]
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    df[['open', 'high', 'low', 'close', 'volume']] = df[['open', 'high', 'low', 'close', 'volume']].astype(float)

    os.makedirs("data/raw_candles", exist_ok=True)
    df.to_csv("data/raw_candles/BTCUSDT_15m.csv", index=False)
    print("Saved BTCUSDT 15m candles to data/raw_candles/")

if __name__ == "__main__":
    get_binance_klines()
