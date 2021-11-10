from pandas import DataFrame


class Backing(object):
    # 总余额
    total_account = 1000
    account_ratio = .99

    def __init__(self, df: DataFrame):
        self.df = df
        return
