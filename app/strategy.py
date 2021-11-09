from numpy import NaN
from pandas import DataFrame

import pandas_ta as ta
from .qtpylib import indicators as qtpylib


class myCout(object):

    def __init__(self, kline=[]):
        dataframe = self.populate_indicators(kline)
        a = self.populate_buy_trend(dataframe)

        return

    def populate_indicators(self, dataframe: DataFrame):
        dataframe['adx'] = ta.ADX(dataframe)
        # MACD
        macd = ta.MACD(dataframe)
        dataframe['macd'] = macd['macd']
        dataframe['macdsignal'] = macd['macdsignal']
        dataframe['macdhist'] = macd['macdhist']
        print(dataframe)

        # a
        return dataframe

    def populate_buy_trend(self, dataframe: DataFrame) -> DataFrame:
        dataframe.loc[
            (

                (qtpylib.crossed_above(dataframe['macdsignal'], 0)) &
                (dataframe['volume'] > 0)
            ),
            'buy'] = 1
        return dataframe

    def populate_sell_trend(self, dataframe: DataFrame) -> DataFrame:
        """
        基于TA指标，为给定的数据帧填充sell信号
        :param dataframe:用指示器填充的dataframe
        :param元数据:附加信息，如当前交易的对
        :return: DataFrame with buy列
        """

        dataframe.loc[
            (
                # (qtpylib.crossed_below(dataframe['macd'] ,0)) &
                (qtpylib.crossed_below(dataframe['macdsignal'], 0)) &
                (dataframe['volume'] > 0)
            ),
            'sell'] = 1
        return dataframe
