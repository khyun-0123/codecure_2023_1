import requests
import json

slack_webhook_url = "https://hooks.slack.com/services/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"

def sendSlackWebHook(strText):
    headers = {
        "Content-type" : "application/json"
    }
    data = {
        "text" : strText
    }
    res = requests.post(slack_webhook_url, headers=headers, data = json.dumps(data))

    if(res.status_code == 200):
        return "OK"
    else:
        return "Error"
print(sendSlackWebHook("안녕하세요 파이썬에서 보내는 메시지입니다."))