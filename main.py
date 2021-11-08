
import threading
import time


def main(self):
    print('服务开始运行！')

    while True:
        time.sleep(1)
        thread()


def thread():
    localtime = time.asctime(time.localtime(time.time()))
    print("本地时间为 :", localtime)
    return


if __name__ == '__main__':
    main(None)
