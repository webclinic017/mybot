from numpy import NaN
from pandas import DataFrame

import talib.abstract as ta
import pandas as pd

from app.qtpylib import indicators as qtpylib
from app.strategy import myCout as strategy


class myCout(strategy):

    def populate_indicators(self, dataframe: DataFrame):
        dataframe['adx'] = ta.ADX(dataframe)

        # # Plus Directional Indicator / Movement
        dataframe['plus_dm'] = ta.PLUS_DM(dataframe)
        dataframe['plus_di'] = ta.PLUS_DI(dataframe)

        # # Minus Directional Indicator / Movement
        dataframe['minus_dm'] = ta.MINUS_DM(dataframe)
        dataframe['minus_di'] = ta.MINUS_DI(dataframe)
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

                (qtpylib.crossed_above(dataframe['plus_dm'], dataframe['minus_dm'])) &
                (dataframe['volume'] > 0) &
                (dataframe['adx'] > 20)
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
                (qtpylib.crossed_above(dataframe['minus_dm'], dataframe['plus_dm'])) &
                (dataframe['volume'] > 0) |
                (dataframe['adx'] > 60)
            ),
            'sell'] = 1
        return dataframe
