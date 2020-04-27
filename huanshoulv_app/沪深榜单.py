import requests


class shares():
    def __init__(self):
        # https://serverplus.huanshoulv.com/aimapp/stock/dashboardHS?device_id=XpprLkoR4xoDAFhbrtS8JoyH&device_token=160a3797c89d4f3de56&appversion=andr-1.9.7.5&hsl_id=5d4c0e77e5863f5402011dd0&div=ANDH010975&open_uuid=XpprLkoR4xoDAFhbrtS8JoyH&channel=hsl-app&sdk_int=29&width=1080
        self.url = 'https://serverplus.huanshoulv.com/aimapp/stock/dashboardHS?device_id=XpprLkoR4xoDAFhbrtS8JoyH&device_token=160a3797c89d4f3de56&appversion=andr-1.9.7.5&hsl_id=5d4c0e77e5863f5402011dd0&div=ANDH010975&open_uuid=XpprLkoR4xoDAFhbrtS8JoyH&channel=hsl-app&sdk_int=29&width=1080'
        self.headers = {
            'User-Agent': '5xbiPfvm851PZfJtTUmgeQ',
            'appversion': '1.9.7.5',
            'deviceId': 'XpprLkoR4xoDAFhbrtS8JoyH',
            'mobiledevice': '2',
            'userId': '5d4c0e77e5863f5402011dd0',
            'Host': 'serverplus.huanshoulv.com',
            'Accept-Encoding': 'gzip',
            'Connection': 'keep-alive'
        }

    def get_data(self):
        request = requests.get(url=self.url, headers=self.headers).text
        print(request)
        return request

    def get_pages(self, request):
        # increaseData 涨幅榜
        js = eval(request)
        for i in range(1, 11):
            print('%s %.2f' % (js['data']['increaseData'][i][2], js['data']['increaseData'][i][3]))
            # print('%s', js['data']['increaseData'][i][2])
            if js['data']['increaseData'][i][3] != 0:
                if i != 10:
                    continue
                else:
                    print("涨幅榜数据清空正常")
            else:
                print("数据清空异常")
                break

        # for i in range(10):
        #     if js['data']['increaseData'][i][3] == 0:
        #         continue
        #     else:
        #         print("数据清空异常")
        #         break


if __name__ == '__main__':
    s = shares()
    s.get_pages(s.get_data())
