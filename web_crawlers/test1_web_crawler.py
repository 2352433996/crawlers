import requests

if __name__ == "__main__":
    # 指定URL http://192.168.1.105:8000/web_crawlers/sogou.html
    url = "https://www.sogou.com/"
    # 发起请求
    response = requests.get(url=url)
    # 获取响应参数
    page_text = response.text
    print(page_text, end='\r\n')
    # 持久化存储
    with open("./sogou.html", "w", encoding="utf-8")as fp:
        fp.writelines(page_text)
    print("爬取数据结束！！！")
