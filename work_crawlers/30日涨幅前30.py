import requests


class shares():
    def __init__(self):
        # http://goserver.huanshoulv.com/aimapp/board/pxchangerateboard?sort_field_name=range_px_change_rate&sort_type=-1&board_type=30&page=1&page_count=20&div=ANDH010974&device_id=WtXerQNk1BoDAJwcljCxlbaA&device_token=170976fa8ad01482290&channel=hsl-app&width=1080&sign=c438bbe0a655fc81c93bb6607032400f&appversion=1.9.7.4&open_uuid=WtXerQNk1BoDAJwcljCxlbaA&sdk_int=28&ts=1586506931332
        self.url = 'http://goserver.huanshoulv.com/aimapp/board/pxchangerateboard'
        self.headers = {
            'User-Agent': 'CypioLzfI0DkRIkmoVY8Qw',
            'appversion': '1.9.7.4',
            'deviceId': 'WtXerQNk1BoDAJwcljCxlbaA',
            'mobiledevice': '2',
            'Host': 'goserver.huanshoulv.com',
            'Accept-Encoding': 'gzip',
            'Connection': 'keep-alive'
        }

    def get_data(self):
        # 拼起来的链接会报错
        da = {
            'sort_field_name': 'range_px_change_rate',
            'sort_type': '-1',
            'board_type': '30',
            'page': '1',
            'page_count': '30',
            'div': 'ANDH010974',
            'device_id': 'WtXerQNk1BoDAJwcljCxlbaA',
            'user_id': '5d356184efc1b0635f03bdcb',
            'hsl_id': '5d356184efc1b0635f03bdcb',
            'device_token': '170976fa8ad01482290',
            'channel': 'hsl-app',
            'width': '1080',
            'sign': '1c8acf4b30cc465c82cba56b5a941541',
            'appversion': '1.9.7.4',
            'open_uuid': 'WtXerQNk1BoDAJwcljCxlbaA',
            'sdk_int': '28',
            'ts': '1586409901311'
        }
        request = requests.get(url=self.url, params=da, headers=self.headers).text
        print(request)
        return request

    def get_pages(self, request, n):
        js = eval(request)
        for i in range(n):
            print("%s %s %.2f" % (js['data']['list'][i][0], js['data']['list'][i][1], js['data']['list'][i][12]))


if __name__ == '__main__':
    s = shares()

    s.get_pages(s.get_data(), 30)
