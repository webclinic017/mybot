from .BinanceAPI import BinanceAPI as http
import time
from pandas import DataFrame
from config.strategy import myCout
import pandas as pd


class App(object):

    def __init__(self, *args):

        return

    def runBot(self):
        self.kline = http().getKline()
        # 获取dataFrame对象
        self.df = myCout(kline=self.filerDataFrame()).dataframe
        self.is_buy_sell()

    def checktime(self):
        servertime = int(http().getSeverTime()/1000)
        localtime = int(time.time())
        cha = servertime - localtime
        if cha > 10:
            print("当前时间差太大")
        else:
            print('核对时间成功')
        return cha < 10

    # 监听买入卖出函数
    def is_buy_sell(self) -> bool:
        data = self.df.max()
        self.df.to_csv('my1.csv')
        a = self.df.loc[self.df.index[-1]]
        print(a['buy'])
        print(a['sell'])
        return True

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

        return df
