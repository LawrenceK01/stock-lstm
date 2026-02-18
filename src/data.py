import pandas as pd

def load_data():
    df = pd.read_csv("data/stocks.csv")
    df["Date"] = pd.to_datetime(df["Date"])
    return df

def compute_returns(df):
    stock_cols = ["AMZN", "DPZ", "BTC", "NFLX"]
    return df[stock_cols].pct_change()

# Scale asset values between -1 and 1
from sklearn.preprocessing import StandardScaler


scaler = StandardScaler()
scaled_data = scaler.fit_transform(df_returns[stock_cols])

