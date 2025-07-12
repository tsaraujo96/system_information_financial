import numpy as np
from scipy.optimize import fmin
from scipy.stats import norm

price = 58.14
strike = 60
r = 0.045
T = 8 / 252
pm = 0.89


def ImpliedVolatilityPut(s):
    d1 = ((np.log(price / strike) + (r + 0.5 * s[0] ** 2) * T) / (s[0] * np.sqrt(T)))
    d2 = ((np.log(price / strike) + (r - 0.5 * s[0] ** 2) * T) / (s[0] * np.sqrt(T)))
    of = (strike * np.exp(-r * T) * norm.cdf(-d2) - price * norm.cdf(-d1)) - pm
    val = of ** 2
    print("[σ]=", s, ", Object Function Value:", val)
    return (val)



def ImpliedVolatilityCall(s):
    d1 = (np.log(price / strike) + (r + 0.5 * s[0] ** 2) * T) / (s[0] * np.sqrt(T))
    d2 = d1 - s[0] * np.sqrt(T)
    # Fórmula para call:
    of = (price * norm.cdf(d1) - strike * np.exp(-r * T) * norm.cdf(d2)) - pm
    val = of ** 2
    print("[σ]=", s, ", Object Function Value:", val)
    return val

s = fmin(ImpliedVolatilityCall, [0.3])
