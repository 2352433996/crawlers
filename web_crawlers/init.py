# 初始框架
import requests
import json

if __name__ == "__main__":
    url = ''
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
    }
    params = {
       '': ''
    }
    response = requests.get(url=url, params=params, headers=headers)
    list_data = response.json()

    fp = open('filename.json', 'w', encoding='utf-8')
    json.dump(list_data, fp, ensure_ascii=False)

    print(list_data)
    print("打印完成！！！")
