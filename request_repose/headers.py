import requests


class post_Header():

    # 发送包含headers的post请求
    def t_post(self):
        url = 'https://www.wanandroid.com/user/login'
        header = {'User-Agent': 'Mozilla/5.0'}
        payload = {'username': 'liangchao', 'password': '123456'}
        # 获取请求后的消息返回体
        rsp = requests.post(url=url, data=payload, headers=header)
        if rsp.status_code != 200:
            return -1, ''
        print(rsp.text)
        # 将返回的字典格式数据转化为json
        json1 = rsp.json()
        errorCode = json1['errorCode']
        if errorCode == 0:
            # 提取json中的部分数据以备后用
            publicName = json1['data']['publicName']
            print(publicName)
            username = json1['data']['username']
            return errorCode, username, publicName
        else:
            return errorCode, '', ''
    def duanyan(self):
        list1 = self.t_post()
        try:
            errorCode1 = list1[0]
            username = list1[1]
            #username = 'kk'
            publicName = list1[2]
            if errorCode1 == 0:
                if username == publicName:
                    print('断言登陆成功')
                else:
                    print('登陆使用的用户名与返回的用户名不一致，登陆失败了')
            else:
                print("errorCode不等于0，登陆失败了")
        except Exception as n:
            print(n)
            print("登陆失败了")

if __name__ == '__main__':
    req = post_Header()
    #req.t_post()
    req.duanyan()
