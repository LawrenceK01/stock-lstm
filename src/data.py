import pandas as pd
import numpy as np

def load_data():
    df = pd.read_csv("../data/portfolio_data.csv")
    df["Date"] = pd.to_datetime(df["Date"])
    df = df.sort_values("Date")
    df = df.set_index("Date")
    return df

def compute_returns(df):
    stock_cols = ["AMZN", "DPZ", "BTC", "NFLX"]
    return df[stock_cols].pct_change()

def create_sequences(data, window_size=30):
    X, y = [], []
    for i in range(len(data) - window_size):
        X.append(data[i:i+window_size])
        y.append(data[i+window_size])
    return np.array(X), np.array(y)

def scale_data(data):
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    return scaler.fit_transform(data)


