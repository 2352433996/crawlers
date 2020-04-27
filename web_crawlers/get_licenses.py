from license import df
import requests


class get_lic():

    def __init__(self):
        self.url = 'http://125.35.6.84:81/xk/itownet/portalAction.do'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
        }

    def get_license(self, id):
        self.params = {
            'method': 'getXkzsById',
            'id': id
        }
        response = requests.post(url=self.url, data=self.params, headers=self.headers).text
        return response


if __name__ == "__main__":
    g = get_lic()
    f = open("化妆品许可证书.txt", "w", encoding="utf-8")
    for ID in df.ary:
        f.write(g.get_license(ID)+'\n')

    f.close()
    print("写入文件完成")
