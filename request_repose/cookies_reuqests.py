import requests

class Cookies_requests:
    def one_cookis(self):
        url1 = 'https://www.wanandroid.com/user/login'
        url2 = 'https://www.wanandroid.com/lg/todo/list/0'
        header = {'User-Agent': 'Mozilla/5.0'}
        payload = {'username': 'liangchao', 'password': '123456'}
        r = requests.post(url=url1, data=payload)
        cookies = r.cookies
        #print(cookies)
        #print(r.text)
        r2 = requests.get(url2, cookies=cookies)
        reuslt = r2.text.find('已完成')
        if reuslt != -1:
            print('ssssssssaasasasas')
        print(r2.status_code)
        #print(r2.text)
if __name__ == '__main__':
    c1 = Cookies_requests().one_cookis()
