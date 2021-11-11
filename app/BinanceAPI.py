

from .myrequest import *
from .MyExcepcation import MyError
from my_config import config


class BinanceAPI(object):
    baseurl = "https://api.binance.com"
    furl = "https://fapi.binance.com"
    # furl = "https://testnet.binancefuture.com"
    pair = config.pair
    interval = config.interval

    def __init__(self, *args):

        # server_res = self.get_server_time()
        # res = self.order()
        return

    # z账户信息
    def get_user_data(self):
        res = send_signed_request("GET", '/fapi/v2/account',
                                  payload={"recvWindow": 5000},
                                  baseurl=self.furl)
        return res
    # 查询当前挂单

    def get_open_order(self):
        res = send_signed_request(
            "GET", '/fapi/v1/openOrder',  payload={"symbol": self.pair}, baseurl=self.furl)
        return res

    # 获取服务器时间

    def get_server_time(self):
        res = send_public_request(
            url_path='/fapi/v1/time', baseurl=self.furl)
        return res['serverTime']

    #  获取kline
    def get_kline(self):
        res = []
        res = send_public_request(url_path="/fapi/v1/klines",
                                  baseurl=self.furl, payload={"symbol": self.pair, "interval": self.interval})
        return res

    # 下单
    def order(self):
        res = send_signed_request("POST", '/fapi/v1/order/test',
                                  payload={
                                      "recvWindow": 3000,
                                      "symbol": self.pair,
                                      "side": "BUY",
                                      "type": "MARKET",
                                      "quantity": 0.01
                                  },
                                  baseurl=self.furl)
        return res
