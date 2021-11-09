import requests 
import json
headers={'Content-Type': 'application/json'} 
class Ding(object):
    def __init__(self, *args):
        return
    def send_message(self,a):
        data = {
            "msgtype": "text",
            "text": {"content": a},
            "isAtAll": True}
        res = requests.post("https://oapi.dingtalk.com/robot/send?access_token=34320162376fd77b0bb27fe6dadb76cc65c92686dfe5ce9d9a6d300aca1c65cc",
        headers=headers,
        data=json.dumps(data)
        )
        print(res.text)
        return res