from pandas.core.frame import DataFrame
import math


# 生成csv
def getbuy_or_selcsv(df: DataFrame, name: str):
    df.to_csv(name+'.csv')
