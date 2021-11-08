
from .myrequest import MyHttpClient


class BinanceAPI(object):
    def __init__(self, *args):
        self.http = MyHttpClient()
        s = self.http.get("/sapi/v1/system/status", None)
        print(s)
        return
