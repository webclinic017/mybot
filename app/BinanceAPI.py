
from pandas.core.arrays import integer
from .myrequest import MyHttpClient
from .MyExcepcation import MyError


class BinanceAPI(object):
    baseurl = "https://api.binance.com"
    furl = "https://fapi.binance.com"
    pair = "FILUSDT"
    interval = "5m"

    def __init__(self, *args):
        self.http = MyHttpClient()
        # s = self.http.get("/sapi/v1/system/status", None)
        # print(s)
        self.getKline()
        return

    def getSeverTime(self):
        res = self.http.get(url='/fapi/v1/time', baseurl=self.furl)
        return res['serverTime']

    #  合约kline
    def getKline(self):
        res = self.http.get(url="/fapi/v1/klines",
                            baseurl=self.furl, query_dict={"symbol": self.pair, "interval": self.interval})
        if res is not None:
            return res
        else:
            raise MyError('请检查 pair or interval')
