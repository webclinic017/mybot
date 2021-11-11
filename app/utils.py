from pandas.core.frame import DataFrame
import time
import datetime

import math


# 生成csv
def getbuy_or_selcsv(df: DataFrame, name: str):
    df.to_csv(name+'.csv')

# 生成ms时间戳


def make_local_ms_imestamp():
    t = time.time()
    return int(round(t * 1000))

# 时间转化函数


def format_time(self, timestamp):
    # 转换成localtime
    time_local = time.localtime(int(timestamp/1000))
    # 转换成新的时间格式(精确到秒)
    dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
    return str(dt)
