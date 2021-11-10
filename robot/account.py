
from pandas import DataFrame


class account(object):
    # 总余额
    total_accunt = 1000

    def __init__(self, df: DataFrame):
        self.df = df
        return
