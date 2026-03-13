def detect_regime(df):
    """
    Detect AI market regime based on average momentum
    """

    momentum = df["Daily %"].mean()

    if momentum > 2:
        regime = "AI SUPER BULL"

    elif momentum > 0.5:
        regime = "AI EXPANSION"

    elif momentum > -1:
        regime = "NEUTRAL"

    else:
        regime = "RISK OFF"

    return regime, momentum


def revenue_projection():
    """
    Project AI ecosystem revenue 16 months forward
    """

    current_revenue = 1.56e12
    growth_rate = 0.18
    months = 16 / 12

    future = current_revenue * (1 + growth_rate) ** months

    return future
