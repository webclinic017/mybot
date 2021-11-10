from app.utils import getbuy_or_selcsv
from pandas import DataFrame


# 导出csv的函数


class CSV(object):
    def __init__(self, df: DataFrame):
        self.df = df
        return

    def export_sell_csv(self):
        getbuy_or_selcsv(
            df=self.df[(self.df.sell == 1)], name="sell")

    def export_buy_csv(self):
        getbuy_or_selcsv(
            df=self.df[(self.df.buy == 1)], name="buy")

    def export_all_csv(self):
        getbuy_or_selcsv(
            df=self.df, name="data")
