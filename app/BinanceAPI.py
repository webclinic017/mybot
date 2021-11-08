
from request import MyHttpClient


class BinanceAPI(object):
    def __init__(self, *args):
        self.http = MyHttpClient()
        s = self.http.get("/fapi/v1/ping")
        print(s)
        return
