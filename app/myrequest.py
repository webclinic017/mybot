from urllib.parse import urlencode
import json
import requests
import hashlib
import time
import hmac


""" This is a very simple script working on Binance API

- work with USER_DATA endpoint with no third party dependency
- work with testnet

Provide the API key and secret, and it's ready to go

Because USER_DATA endpoints require signature:
- call `send_signed_request` for USER_DATA endpoints
- call `send_public_request` for public endpoints

```python

python futures.py

```

"""

KEY = "yiQn1StKCKchvq6SNveMgPcML29ZX5rI8HDs1N1OFW3j95hdKcVPlsXEbth3prxN"
SECRET = 'sqjSGvUgdlRfddkl7Vz1sDQPwk8TrpJbdctE8God7s2DqMtJyENBRBsxEK5Y3GIE'
# BASE_URL = 'https://fapi.binance.com' # production base url
BASE_URL = 'https://testnet.binancefuture.com'  # testnet base url

''' ======  begin of functions, you don't need to touch ====== '''


def hashing(query_string):
    return hmac.new(SECRET.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()


def get_timestamp():
    return int(time.time() * 1000)


def dispatch_request(http_method):
    session = requests.Session()
    session.headers.update({
        'Content-Type': 'application/json;charset=utf-8',
        'X-MBX-APIKEY': KEY
    })
    return {
        'GET': session.get,
        'DELETE': session.delete,
        'PUT': session.put,
        'POST': session.post,
    }.get(http_method, 'GET')

# used for sending request requires the signature


def send_signed_request(http_method, url_path, payload={}, baseurl=BASE_URL):
    query_string = urlencode(payload)
    # replace single quote to double quote
    query_string = query_string.replace('%27', '%22')
    if query_string:
        query_string = "{}&timestamp={}".format(query_string, get_timestamp())
    else:
        query_string = 'timestamp={}'.format(get_timestamp())

    url = baseurl + url_path + '?' + query_string + \
        '&signature=' + hashing(query_string)
    print("{} {}".format(http_method, url))
    params = {'url': url, 'params': {}}
    response = dispatch_request(http_method)(**params)
    return response.json()

# used for sending public data request


def send_public_request(url_path, payload={}, baseurl=BASE_URL):
    query_string = urlencode(payload, True)
    url = baseurl + url_path
    if query_string:
        url = url + '?' + query_string
    print("{}".format(url))
    response = dispatch_request('GET')(url=url)
    return response.json()


''' ======  end of functions ====== '''
# https://github.com/binance/binance-signature-examples/blob/master/python/futures.py
