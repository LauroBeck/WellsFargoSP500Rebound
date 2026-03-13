from portfolio_analytics import portfolio_returns, region_breakdown
from portfolio_config import weights, regions
from nasdaq_feed import get_market_data


def run_portfolio():

    prices = get_market_data()

    port_ret = portfolio_returns(prices, weights)

    region_perf = region_breakdown(regions, prices)

    print("\nPORTFOLIO PERFORMANCE\n")

    print("Average Portfolio Return:", round(port_ret.mean()*100,2), "%")

    print("\nRegional Breakdown")

    print(region_perf.round(2))


if __name__ == "__main__":
    run_portfolio()
