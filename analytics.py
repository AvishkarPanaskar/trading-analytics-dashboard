import pandas as pd
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller

# Z-score function
def zscore(series):
    return (series - series.mean()) / series.std()

# Hedge ratio via OLS
def hedge_ratio(x, y):
    x = sm.add_constant(x)
    model = sm.OLS(y, x).fit()
    return model.params[1]

# Spread calculation
def spread(p1, p2, beta):
    return p1 - beta * p2

# Price stats
def price_stats(df):
    return {
        "mean": df.price.mean(),
        "std": df.price.std(),
        "min": df.price.min(),
        "max": df.price.max()
    }

# ADF test
def adf_test(series):
    result = adfuller(series)
    return result[1]  # p-value
