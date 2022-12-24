
import requests
#请求方法封装类
class Request_mode():

    #get请求方法封装
    def get_mode(self, get_url, get_payload):

        rsp = requests.get(url=get_url, params=get_payload)

        return ''
    #post方法封装
    def post_mode(self):
        return ''
    #put方法封装
    def put_mode(self):
        return ''
    #delete方法封装
    def delete_mode(self):
        return ''
