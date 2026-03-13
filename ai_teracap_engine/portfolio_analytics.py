import pandas as pd

def portfolio_returns(price_df, weights):
    """
    Calculate weighted portfolio returns
    """

    returns = price_df.pct_change().dropna()

    weights_series = pd.Series(weights)

    portfolio_return = (returns * weights_series).sum(axis=1)

    return portfolio_return


def region_breakdown(portfolio_map, price_df):
    """
    Aggregate returns by region
    """

    returns = price_df.pct_change().dropna()

    df = pd.DataFrame(returns)

    df_region = {}

    for ticker, region in portfolio_map.items():
        if region not in df_region:
            df_region[region] = returns[ticker]

        else:
            df_region[region] += returns[ticker]

    region_df = pd.DataFrame(df_region)

    return region_df.mean() * 100
