import json
import requests


# 机器人
def robot(text):
    url = 'https://oapi.dingtalk.com/robot/send?access_token=bc441ce851993e9b815b1fc4eef47737b4a27b1357d4fb8416a9c3d1e573cc8a'
    data = {
        "msgtype": "text",
        "text": {
            # 发送内容
            "content": text
        },
        "at": {
            "atMobiles": [
                "15070484981"
            ],
            "isAtAll": False
        }
    }
    data = json.dumps(data)
    headers = {
        "Content-Type": "application/json",
        "Charset": "UTF-8"
    }
    requests.post(url=url, data=data, headers=headers)
