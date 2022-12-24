import requests
url = 'https://www.wanandroid.com/user/login'
header = {'User-Agent': 'Mozilla/5.0'}
payload = {'username': 'liangchao', 'password': '1234切56'}
# 获取请求后的消息返回体
rsp = requests.post(url=url, data=payload, headers=header)
print(rsp.text)

def t_get():


    pass
def t_post():
    pass
def t_put():
    pass
def t_delete():
    pass