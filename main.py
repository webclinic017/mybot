

from model.order import Order
import time
from app.BinanceAPI import BinanceAPI
from app.myApp import App
import urllib3
urllib3.disable_warnings()
# 版本1.2


def main(self):
    print('服务开始运行！长时间没反应请连接vpn')
    # 校验服务器时间
    bot = App()
    bot.checktime()
    while True:
        bot.runBot()
        time.sleep(1)
        thread()


def thread():
    return


if __name__ == '__main__':
    Order.create_table()
    main(None)
