from numpy import NaN
from pandas import DataFrame

import talib.abstract as ta
import pandas as pd

from app.qtpylib import indicators as qtpylib
from app.strategy import myCout as strategy


class myCout(strategy):

    def populate_indicators(self, dataframe: DataFrame):
        dataframe['adx'] = ta.ADX(dataframe)
        # MACD
        macd = ta.MACD(dataframe)
        dataframe['macd'] = macd['macd']
        dataframe['macdsignal'] = macd['macdsignal']
        dataframe['macdhist'] = macd['macdhist']

        # print(dataframe.style)
        
        # a
        return dataframe

    def populate_buy_trend(self, dataframe: DataFrame) -> DataFrame:
        dataframe.loc[
            (

                (qtpylib.crossed_above(dataframe['macdsignal'], 0)) &
                (dataframe['volume'] > 0)
            ),
            'buy'] = True
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
            'sell'] = True
        return dataframe
