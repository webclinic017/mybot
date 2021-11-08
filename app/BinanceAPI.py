
from .myrequest import MyHttpClient


class BinanceAPI(object):
    baseurl = "https://api.binance.com"
    furl = "https://fapi.binance.com"

    def __init__(self, *args):
        self.http = MyHttpClient()
        # s = self.http.get("/sapi/v1/system/status", None)
        # print(s)
        # self.getTime()
        return

    def getTime(self):
        res = self.http.get(url='/fapi/v1/time', baseurl=self.furl)
        return res['serverTime']
