import requests

access_token = 'DRuHwpTO7UlGjeIKmlhLMiJVhfhrwyqUCSVEDCm-mEnIcJ4NUoP19AqHHYohsRp-4U4BuXdGwTrpQCXbwP8vmwaAN93ZH1-tazmt4C3jMm9qG69mWKBjzMHSfal_XJT2IMIgWBlprWKJKMVwINcX1BsKB--ZADuj7L2uPP-WVFOvRtlP6EhG2OvULYj7bPwwgx5NGYkg2InUj9ERzzVgGA'

url = f'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={access_token}'
data = {
    "touser": "@all",
    "toparty": "@all",
    "totag": "@all",
    "msgtype": "text",
    "agentid": 1000002,
    "text": {
        "content": '测试action'
    },
    "safe": 0,
    "enable_id_trans": 0,
    "enable_duplicate_check": 0,
    "duplicate_check_interval": 1800
}
r = requests.post(url, json=data).json()
print(r.text)
