import pandas as pd

def compute_returns(close):
    """
    Compute latest price and daily return
    """

    returns = close.pct_change() * 100

    df = pd.DataFrame({
        "Price": close.iloc[-1],
        "Daily %": returns.iloc[-1]
    })

    return df
