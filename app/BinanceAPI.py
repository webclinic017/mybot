

from .myrequest import MyHttpClient
from .MyExcepcation import MyError
from my_config import config


class BinanceAPI(object):
    baseurl = "https://api.binance.com"
    furl = "https://fapi.binance.com"
    pair = config.pair
    interval = config.interval

    def __init__(self, *args):
        self.http = MyHttpClient()
        return

    def get_user_data(self):
        res = self.http.get(url='/fapi/v2/account ', baseurl=self.furl)
        return res
    # 获取服务器时间

    def getSeverTime(self):
        res = self.http.get(url='/fapi/v1/time', baseurl=self.furl)
        return res['serverTime']

    #  获取kline
    def getKline(self):
        res = self.http.get(url="/fapi/v1/klines",
                            baseurl=self.furl, query_dict={"symbol": self.pair, "interval": self.interval})
        if res is not None:
            return res
        else:
            raise MyError('请检查 pair or interval')
