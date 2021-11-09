import requests
from requests.adapters import HTTPAdapter
import json
from .MyExcepcation import MyError


class MyHttpClient:

    def __init__(self, timeout=4):
        """
        :param timeout: 每个请求的超时时间
        """
        s = requests.Session()
        # : 在session实例上挂载Adapter实例, 目的: 请求异常时,自动重试
        s.mount('http://', HTTPAdapter(max_retries=3))
        s.mount('https://', HTTPAdapter(max_retries=3))

        # : 设置为False, 主要是HTTPS时会报错, 为了安全也可以设置为True
        s.verify = False
        # : 公共的请求头设置
        s.headers = {
            "apiKey": "yiQn1StKCKchvq6SNveMgPcML29ZX5rI8HDs1N1OFW3j95hdKcVPlsXEbth3prxN",
            "secret": "sqjSGvUgdlRfddkl7Vz1sDQPwk8TrpJbdctE8God7s2DqMtJyENBRBsxEK5Y3GIE",
        }

        # : 挂载到self上面
        self.s = s
        self.timeout = timeout

    def get(self, url, query_dict=None, baseurl="https://api.binance.com"):
        """GET

        :param url:
        :param query_dict: 一般GET的参数都是放在URL查询参数里面
        :return:
        """
        url = baseurl+url
        res = self.s.get(url=url, params=query_dict)
        if res.status_code == 200:
            return json.loads(res.text)
        else:
            return None

    def post(self, url, form_data=None, body_dict=None, baseurl="https://api.binance.com"):
        """POST

        :param url:
        :param form_data: 有时候POST的参数是放在表单参数中
        :param body_dict: 有时候POST的参数是放在请求体中(这时候 Content-Type: application/json )
        :return:
        """
        url = baseurl+url

        form = self.s.post(url, data=form_data)
        body = self.post(url, json=body_dict)
        if form_data:
            return json.loads(form.text)
        if body_dict:
            return body

    def __del__(self):
        """当实例被销毁时,释放掉session所持有的连接

        :return:
        """
        if self.s:
            self.s.close()
