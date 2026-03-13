import numpy as np
from scipy.stats import norm


def black_scholes(S, K, T, r, sigma):

    d1 = (np.log(S/K) + (r + sigma**2/2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)

    call = S*norm.cdf(d1) - K*np.exp(-r*T)*norm.cdf(d2)
    put = K*np.exp(-r*T)*norm.cdf(-d2) - S*norm.cdf(-d1)

    return call, put


if __name__ == "__main__":

    S = 5200    # SP500 level
    K = 5300    # strike
    T = 0.25    # 3 months
    r = 0.05
    sigma = 0.20

    call, put = black_scholes(S, K, T, r, sigma)

    print("\nSP500 OPTIONS MODEL\n")

    print("Call Price:", round(call,2))
    print("Put Price:", round(put,2))

