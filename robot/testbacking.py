from pandas import DataFrame
from app.utils import getbuy_or_selcsv


class Backing(object):
    total_account = 1000
    account_ratio = .99

    def __init__(self, df: DataFrame):
        self.df = df
        self.complate()
        return

    def complate(self):
        df = self.df
        print(df.describe())
        for index, row in df.iterrows():
            if row.buy == 1:
                row
