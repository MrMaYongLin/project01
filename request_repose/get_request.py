
"""
导入requests包
请求
打印返回结果
"""
import requests
class no_payload():
    urls1 = "https://www.baidu.com/"
    urls2 = 'http://www.wanandroid.com'
    r1 = requests.get(url=urls2)
    #print(r1.text)

class have_payload():
    urlu1 = 'http://www.wanandroid.com'
    payload = {'k': 'win'}
    r2 = requests.get(url=urlu1,params=payload)
    print(r2.status_code)
    print(r2.headers)
    print(r2.text)

if __name__ == '__main__':
    pass