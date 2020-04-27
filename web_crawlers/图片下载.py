import requests


class get_photos():
    def __init__(self):
        self.url = "http://image.baidu.com/search/index?ct=201326592&cl=2&st=-1&lm=-1&nc=1&ie=utf-8&tn=baiduimage&ipn=r&rps=1&pv=&fm=rs1&word=%E8%93%9D%E8%89%B2%E8%83%8C%E6%99%AF%E5%9B%BE&oriquery=%E5%9B%BE%E7%89%87&ofr=%E5%9B%BE%E7%89%87&sensitive=0"
        self.heraders = {
            'User-Agent': "Mozilla / 5.0(Macintosh; Intel Mac OS X 10 _14_6) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 80.0 .3987 .163 Safari / 537.36"
        }

    def get_data(self):
        response = requests.get(self.url, headers=self.heraders).text
        print(response)
        return response


if __name__ == '__main__':
    s = get_photos()
    f = open("百度图片.html", "w", encoding="utf-8")
    f.write(s.get_data())
