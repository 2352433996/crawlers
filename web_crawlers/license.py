# 初始框架
import requests
import json
import time


class df():
    def __init__(self):
        self.url = 'http://125.35.6.84:81/xk/itownet/portalAction.do?'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
        }
        self.ary = []

    def data(self, num):
        da = {
            'method': 'getXkzsList',
            'on': 'true',
            'page': num,
            'pageSize': 15,
            'productName': '',
            'conditionType': 1,
            'applyname': '',
            'applysn': ''
        }
        # 发起请求
        response = requests.post(url=self.url, data=da, headers=self.headers).content.decode()

        return response

    def get_id(self, response):
        # print(response)
        d = json.loads(response)

        for c in range(0, 15):
            self.ary.append(d['list'][c]["ID"])
        # ary['EPS_NAME'] = d['list'][0]['EPS_NAME']
        # ary['PRODUCT_SN'] = d['list'][0]['PRODUCT_SN']
        # ary['QF_MANAGER_NAME'] = d['list'][0]['QF_MANAGER_NAME']
        # ary['XK_DATE'] = d['list'][0]['XK_DATE']
        # ary['XC_DATE'] = d['list'][0]['XC_DATE']
        # print(self.ary)
        return self.ary

        # with open('化妆品许可证.html', 'w', encoding='utf-8')as fp:
        #     fp.write(page_text)
        # print("打印完成！！！")

    def get_license(self):
        # print(self.ary)
        pass


# if __name__ == "__main__":

df = df()
pageCount = json.loads(df.data(1))['pageCount']
# print(pageCount)
for n in range(1, pageCount + 1):
    q = df.data(n)
    df.get_id(q)
    time.sleep(1)
    if n == 5:
        break
    else:
        pass

df.get_license()
