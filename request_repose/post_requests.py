import json

import requests
class post_req:
    @staticmethod
    def pos():
        url1 = 'http://httpbin.org/post'
        payload = {'群名': '哈喽', '群号': '2929271246'}
        # 由于payload参数是字典格式的，而接口请求是需要json格式的，所以需要将字典格式转化为json格式
        payload = json.dumps(payload)
        resp = requests.post(url=url1, data=payload)
        #如果不进行转化json，那么在进行post请求的时候需要将data换成json。这个时候python如会自动将字典参数改成json参数下：
        #resp = requests.post(url=url1,json=payload)
        print(resp.text)
post_req.pos()
