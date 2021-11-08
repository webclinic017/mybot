from .BinanceAPI import BinanceAPI as http
import time


class App(object):
    def __init__(self, *args):
        return

    def checktime(self):
        servertime = int(http().getTime()/1000)
        localtime = int(time.time())
        cha = servertime - localtime
        if cha > 10:
            print("当前时间差太大")
        else:
            print('核对时间成功')
        return cha < 10
