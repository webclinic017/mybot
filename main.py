
import threading
import time
from app.BinanceAPI import BinanceAPI
from app.myApp import App


def main(self):
    print('服务开始运行！')
    # 校验服务器时间
    App().checktime()
    while True:
        time.sleep(1)
        thread()


def thread():
    BinanceAPI()
    return


if __name__ == '__main__':
    main(None)
