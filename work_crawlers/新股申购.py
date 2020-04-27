# http://data.eastmoney.com/xg/xg/default.html
# scheduler = BlockingScheduler() #调度器
#             #需要执行的方法（不要括号）    星期一到星期五        14:14:5启动
#     scheduler.add_job(hq.run, 'cron', day_of_week='1-5', hour=14, minute=14, second=5)
#     scheduler.start()

import requests
import json
import time
import ast


class shares():
    def __init__(self):
        self.url = 'http://dcfm.eastmoney.com/em_mutisvcexpandinterface/api/js/get?'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
        }

    def data(self, page):
        da = {
            'type': 'XGSG_LB',
            'token': '70f12f2f4f091e459a279469fe49eca5',
            'st': 'purchasedate,securitycode',
            'sr': '-1',
            'p': page,
            'ps': '50',
            # 'js': 'var yEKATrXe={"pages":(tp),"data":(x)}', 控制返回格式
            'js': 'var yEKATrXe={pages:(tp),data:(x)}',
            'rt': '52794637'
        }
        request = requests.get(url=self.url, params=da, headers=self.headers).text
        # index = request.index('data:')
        # index += 5
        # js = eval(request[index: -1])
        #
        # index2 = request.index('={')
        # index2 += 1
        # js2 = eval(request[index2:])
        # print(js2)
        return request

    def parsing_json(self, request):
        index = request.index('data:')
        index += 5
        js = eval(request[index: -1])
        return js[0]['securityshortname']

    def jsonfy(s: str) -> object:
        # 此函数将不带双引号的json的key标准化
        obj = eval(s, type("js", (dict,), dict(__getitem__=lambda s, n: n))())
        return obj

    def get_pages(self, request):
        # print(request)
        index2 = request.index('={')
        index2 += 1
        # print(index2)
        # print(request[index2:])
        # data1 = ast.literal_eval(request[index2:])
        print(index2)

        data1 = shares.jsonfy(request[index2:])
        print(data1)
        # data1 = request[index2:].replace('pages', '\"pages\"', 1)
        # print(data1['pages'])
        # print(type())
        # js2 = eval(request[index2:-1])
        return data1['pages']


if __name__ == '__main__':
    s = shares()
    # print(s.parsing_json(a))
    pages = s.get_pages(s.data(1))
    for n in range(1, pages):
        print(s.parsing_json(s.data(n)))
        if n == 5:
            break
        else:
            pass
