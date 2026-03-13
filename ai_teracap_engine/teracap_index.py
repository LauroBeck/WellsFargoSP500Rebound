import pandas as pd


def build_teracap_index(close):

    # GPU layer
    gpu = close[["NVDA","AMD"]].pct_change().mean(axis=1)

    # Cloud AI layer
    cloud = close[["MSFT","AMZN","GOOGL","META"]].pct_change().mean(axis=1)

    # Semiconductor supply chain
    semi = close[["TSM","ASML"]].pct_change().mean(axis=1)

    df = pd.DataFrame({
        "GPU": gpu,
        "CLOUD": cloud,
        "SEMI": semi
    })

    # weighted AI index
    df["TERACAP_INDEX"] = (
        df["GPU"] * 0.4 +
        df["CLOUD"] * 0.35 +
        df["SEMI"] * 0.25
    )

    return df
