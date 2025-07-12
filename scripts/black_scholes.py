import math

from scipy.stats import norm

from enum import Enum


class StockType(Enum):
    CALL = 0
    PUT = 1


def _calc_black_scholes(price_paper, strike, time_to_expire, selic, volatility, option_type):

    time_to_expire = time_to_expire / 252

    d1 = (math.log(price_paper / strike) + (selic + 0.5 * volatility ** 2) * time_to_expire) / (volatility * math.sqrt(time_to_expire))
    d2 = d1 - volatility * math.sqrt(time_to_expire)

    if option_type.value == StockType.CALL.value:
        return price_paper * norm.cdf(d1) - strike * math.exp(-selic * time_to_expire) * norm.cdf(d2)

    return strike * math.exp(-selic * time_to_expire) * norm.cdf(-d2) - price_paper * norm.cdf(-d1)


if __name__ == '__main__':

    price_paper = 61
    strike = 60
    time_to_expire = 8
    volatility = 0.38
    selic = 0.045
    option_type = StockType.CALL

    value = _calc_black_scholes(price_paper=price_paper, strike=strike, time_to_expire=time_to_expire,
                                volatility=volatility, selic=selic, option_type=option_type)

    print(round(value, 2))







