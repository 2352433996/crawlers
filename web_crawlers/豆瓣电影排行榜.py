import requests
import json

if __name__ == "__main__":
    url = 'https://movie.douban.com/j/chart/top_list'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
    }
    params = {
        'type': '24',
        'interval_id': '100:90',
        'action': '',
        'start': '0',
        'limit': '20'   # 每次请求的个数
    }
    response = requests.get(url=url, params=params, headers=headers)
    list_data = response.json()
    fp = open('豆瓣电影排行榜.json', 'w', encoding='utf-8')
    json.dump(list_data, fp, ensure_ascii=False)
    print(list_data)
    print("打印完成！！！")
