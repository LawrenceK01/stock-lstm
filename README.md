# Stock Price Prediction with LSTM

This project explores using an LSTM (Long Short-Term Memory) neural network
to predict stock prices from historical time series data.

The goal is not to build a profitable trading system, but to:
- understand time series forecasting
- practice building deep learning models
- evaluate limitations of LSTMs on financial data

## Dataset

Data sourced from Kaggle: (https://www.kaggle.com/datasets/hershyandrew/amzn-dpz-btc-ntfx-adjusted-may-2013may2019/code)

Contains daily prices for 5 stocks.

## Setup

```bash
conda env create -f environment.yml
conda activate stock-lstm
