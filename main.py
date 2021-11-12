

from re import S
import sys
from my_config import config
from model.order import Order
import time
from app.myApp import App
import urllib3
urllib3.disable_warnings()
bot = App()

type = "testbacking"
# 版本1.2

for index, s in enumerate(sys.argv):
    if s == 'main.py':
        continue
    if index == 1:
        type = s
        continue
    s = s.split("=")
    if s[0] == "-t":
        type = s


print('服务开始运行！长时间没反应请连接vpn')


def main(self):
    # 校验服务器时间
    bot.checktime()
    while True:
        bot.runBot()
        time.sleep(1)


if type == 'testbacking':
    bot.testbacking()
elif type == "dev":
    bot.run_dev()
elif type == "pro":
    bot.run_pro()
