from .BinanceAPI import BinanceAPI as http
import time
from pandas import DataFrame
from .strategy import myCout


class App(object):

    def __init__(self, *args):
        self.kline = http().getKline()
        myCout(kline=self.filerDataFrame()
               )

        return

    def checktime(self):
        servertime = int(http().getSeverTime()/1000)
        localtime = int(time.time())
        cha = servertime - localtime
        if cha > 10:
            print("当前时间差太大")
        else:
            print('核对时间成功')
        return cha < 10

    # [
    #   [
    #     1607444700000,      // 开盘时间
    #     "18879.99",         // 开盘价
    #     "18900.00",         // 最高价
    #     "18878.98",         // 最低价
    #     "18896.13",         // 收盘价(当前K线未结束的即为最新价)
    #     "492.363",          // 成交量
    #     1607444759999,      // 收盘时间
    #     "9302145.66080",    // 成交额
    #     1874,               // 成交笔数
    #     "385.983",          // 主动买入成交量
    #     "7292402.33267",    // 主动买入成交额
    #     "0"                 // 请忽略该参数
    #   ]
    # ]

    def filerDataFrame(self):
        df = DataFrame(data=self.kline,
                       dtype=float,
                       columns=[
                           "start_time", "open", "high", "low", "close", "volume",
                           "close_time", "total_vol", "order_nums", "buy_vol", "buy_tatol", "d"
                       ])
        # df.astype(d)
        return df
