# 肯德基官网 http://www.kfc.com.cn/kfccda/index.aspx
import requests

import requests
import json

if __name__ == "__main__":
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
    }
    keyword = input("请输入城市：")
    data = {
        'cname': '',
        'pid': '',
        'keyword': keyword,
        'pageIndex': '1',
        'pageSize': '10'
    }
    response = requests.post(url=url, data=data, headers=headers)
    list_data = response.text

    fp = open(keyword+'肯德基位置.json', 'w', encoding='utf-8')
    fp.write(list_data)
    fp.close()

    print(list_data)
    print("打印完成！！！")
