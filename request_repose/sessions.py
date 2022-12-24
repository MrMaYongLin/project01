import requests

class Session:
    def __init__(self, url, params, headers, cookies, data):
        self.url = url
        self.params = params
        self.header = headers
        self.cookies = cookies
        self.data = data
    def sessions_method(self):
        s = requests.session()
        r1 = s.post(url=url, data=data)
        print(r1.status_code)
        r2 = s.get('https://www.wanandroid.com/lg/todo/list/0')
        print(r2.status_code)
        print(r2.text)
if __name__ == '__main__':
    url = 'https://www.wanandroid.com/user/login'
    params = ''
    headers = ''
    cookies = ''
    data = {'username': 'liangchao', 'password': '123456'}
    s1 = Session(url, params, headers, cookies, data)
    s1.sessions_method()
