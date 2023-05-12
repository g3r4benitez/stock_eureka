import requests
from ratelimit import limits

from app.core.config import ALPHA_URL, ALPHA_APIKEY
from app.core.config import REQUEST_PERSECOND, REQUEST_PERMINUTE, ONE_SECOND, ONE_MINUTE


class AlphaService:

    def __init__(self):
        pass

    #@limits(calls=REQUEST_PERSECOND, period=ONE_SECOND)
    @limits(calls=REQUEST_PERMINUTE, period=ONE_MINUTE)
    def get_stock(self, simbol):
        """
        Call to Alpha Vantage services and get Time Series Daily
        :param simbol:
        :return:
        """
        url = f"{ALPHA_URL}/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={simbol}&outputsize=compact&apikey={ALPHA_APIKEY}"

        r = requests.get(
            url=url,
        )
        last_market_info = self.get_last_market_info(r.json())

        return last_market_info

    def get_last_market_info(self, market):
        """
        Process market info and return the last market prices (open, high, low), and the variation between last market
        and the previous date.
        :param market: market time series
        :return: a dictionary
        """
        ts = market["Time Series (Daily)"]
        lmarket = list(market["Time Series (Daily)"].keys())
        last = lmarket[0]
        prev = lmarket[1]
        variation = abs(float(ts[last]["4. close"]) - float(ts[prev]["4. close"]))
        return {
            "Open price": ts[last]["1. open"],
            "Higher price": ts[last]["2. high"],
            "Lower price": ts[last]["3. low"],
            "Variation": f"{variation:.2f}"
        }



