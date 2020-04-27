import requests

if __name__ == "__main__":
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36;'
    }
    url = "https://voice.baidu.com/act/newpneumonia/newpneumonia/"
    params = {
        "from": "osari_pc_1"
    }
    response = requests.get(url=url, params=params, headers=headers)
    data = response.text
    with open("疫情详细地图.html", "w", encoding="utf-8") as fp:
        fp.write(data)
        print("爬取数据成功！！!")
