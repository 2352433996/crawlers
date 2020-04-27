import requests

if __name__ == "__main__":
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
    }
    # 指定URL http://192.168.1.105:8000/web_crawlers/sogou.html
    url = "https://voice.baidu.com/act/newpneumonia/newpneumonia/?"
    keywords = input("请输入搜索关键字：")
    params = {
        'from': "osari_pc_1"
    }
    # 发起请求
    response = requests.get(url=url, params=params, headers=headers)
    # 获取响应参数
    page_text = response.text
    print(page_text, end='\r\n')
    # 持久化存储
    file_name = keywords+".html"

    with open(file_name, "w", encoding="utf-8")as fp:
        fp.writelines(page_text)
    print("爬取数据结束！！！")
