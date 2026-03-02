# Comparing Model Performance on Stock Market Data
This project compares the performance of ridge regression, lasso regression, ElasticNet, an AutoRegressive model, and a LSTM on a relatively small, noisy dataset of stock prices. We compare the performance of these models to 2 baselines: A naive baseline (predict tomorrow = today) and a rolling mean baseline (predict tomorrow = mean of previous N returns).
All models and baselines are evaluated using mean squared error (MSE), a standard loss metric for linear models and neural nets. 
MSE is calculated via $MSE = \frac{1}{N}\sum_{i=1}^{N} (y_i - \hat y_i)^2$
RMSE is also calculated where relevant, where $RMSE = \sqrt{MSE}$

## Dataset

Data sourced from Kaggle: (https://www.kaggle.com/datasets/hershyandrew/amzn-dpz-btc-ntfx-adjusted-may-2013may2019/code)

Contains 1520 daily prices for 5 stocks (Amazon, Domino's Pizza, Bitcoin, and Netflix) from 2013 to 2019.

## Setup

```bash
conda env create -f environment.yml
conda activate stock-lstm
