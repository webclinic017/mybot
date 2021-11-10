from numpy import NaN
from pandas import DataFrame

import talib.abstract as ta
import pandas as pd

from .qtpylib import indicators as qtpylib

import numpy as np


class myCout(object):

    def __init__(self, kline=[]):
        dataframe = self.populate_indicators(kline)
        dataframe = self.populate_buy_trend(dataframe)
        dataframe = self.populate_sell_trend(dataframe)
        # dataframe.to_csv('my.csv')
        # dataframe[['buy', 'sell']] = dataframe[[
        #     'buy', 'sell']].astype(np.bool_)
        self.dataframe = dataframe

    def populate_indicators(self, dataframe: DataFrame):
        dataframe['adx'] = ta.ADX(dataframe)
        # MACD
        macd = ta.MACD(dataframe)
        dataframe['macd'] = macd['macd']
        dataframe['macdsignal'] = macd['macdsignal']
        dataframe['macdhist'] = macd['macdhist']

        # a
        return dataframe

    def populate_buy_trend(self, dataframe: DataFrame) -> DataFrame:
        return dataframe

    def populate_sell_trend(self, dataframe: DataFrame) -> DataFrame:
        """
        基于TA指标，为给定的数据帧填充sell信号
        :param dataframe:用指示器填充的dataframe
        :param元数据:附加信息，如当前交易的对
        :return: DataFrame with buy列
        """

        return dataframe
