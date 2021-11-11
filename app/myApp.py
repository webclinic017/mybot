from .BinanceAPI import BinanceAPI as http
import time
from pandas import DataFrame
from config.strategy import myCout
import pandas as pd
from .dingding import Ding
import time
import datetime
from .utils import getbuy_or_selcsv, format_time
import numpy as np
from model.order import Order
# 模拟运行 真实运行 回测

# state 状态 0 开始 1查询数据 2


class App(object):

    state = ""

    def __init__(self, *args):

        return

    # 设在data数据
    def set_data_frame(self):
        self.kline = http().get_kline()
        # 获取dataFrame对象
        self.df = myCout(kline=self.filerDataFrame()).dataframe
        self.get_csv(self.df)
        return

    def runBot(self):
        self.set_data_frame()
        # self.is_buy_sell()

    # 获取csv
    def get_csv(self, df: DataFrame):
        # 最新的订单
        new_order = df[(self.df.buy == 1)]
        Order().add_order(side="BUY", start_time=df.start_time)
        getbuy_or_selcsv(
            df=df[(self.df.buy == 1)], name="buy")
        getbuy_or_selcsv(
            df=df[(self.df.sell == 1)], name="sell")
    # 获取

    # 核对服务器时间
    def checktime(self):
        servertime = int(http().get_server_time()/1000)
        localtime = int(time.time())
        cha = servertime - localtime
        if cha > 10:
            print("当前时间差太大")
        else:
            print('核对时间成功')
        return cha < 10

    # 监听买入卖出函数
    def is_buy_sell(self):
        df = self.df.loc[self.df.index[-1]]
        if df['buy'] == 1:

            Ding().send_message("操作 当前买入 fil 价格:" +
                                str(df["close"])+" 时间:"+format_time(df["close_time"]))
        if df['sell'] == 1:
            Ding().send_message("操作 当前卖出 fil 价格:" +
                                str(df["close"])+" 时间:"+format_time(df["close_time"]))

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
    # DataFrame 转化成
    def filerDataFrame(self):
        df = DataFrame(data=self.kline,
                       dtype=float,
                       columns=[
                           "start_time", "open", "high", "low", "close", "volume",
                           "close_time", "total_vol", "order_nums", "buy_vol", "buy_tatol", "d"
                       ])
        df[['start_time', 'close_time']] = df[[
            'start_time', 'close_time']].astype(np.int_)
        return df
