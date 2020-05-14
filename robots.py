import json
import requests


# 机器人
def robot(text, mobiles=["15070484981"], isAtAll=False):
    url = 'https://oapi.dingtalk.com/robot/send?access_token=bc441ce851993e9b815b1fc4eef47737b4a27b1357d4fb8416a9c3d1e573cc8a'
    data = {
        "msgtype": "text",
        "text": {
            # 发送内容all
            "content": text
        },
        "at": {
            "atMobiles": mobiles,
            "isAtAll": isAtAll   # @所有人时：True，否则为：False
        }
    }
    data = json.dumps(data)
    headers = {
        "Content-Type": "application/json",
        "Charset": "UTF-8"
    }
    requests.post(url=url, data=data, headers=headers)

# robot('测试')
