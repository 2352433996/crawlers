# 百度翻译
#     post请求（携带了参数
#     响应数据类型为json

import json
import requests

if __name__ =="__main__":
    # UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
    }
    # 指定请求头
    post_url = 'https://fanyi.baidu.com/sug'

    word = input("Enter a word:")

    # post请求参数处理（同get请求一致）
    data = {
        'kw': word
    }
    response = requests.post(url=post_url, data=data, headers=headers)
    # 获取响应数据，确认了响应类型为json才可以用.json()方法，通过content-type进行确认
    # content-type: application/json; charset=utf-8
    dic_obj = response.json()

    fp = open(word+'.json', 'w', encoding='utf-8')
    # 持久化存储
    # 中文不能用ASCII码进行编码（ensure_ascii=False）
    json.dump(dic_obj, fp=fp, ensure_ascii=False)
    print(dic_obj)
    print("爬取完成！")

