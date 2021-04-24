import requests
from requests_toolbelt import MultipartEncoder

ID = 'wwbe83b651891d42ff'
SECRET = 'I8Cu09C_men__R_11qboyo7p4c4FJsmgN9OnNijFXBg'


def get_access_token():
    url = f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={ID}&corpsecret={SECRET}'
    r = requests.get(url).json()
    with open('access_token.txt', 'w', encoding='utf-8') as f:
        f.write(r.get('access_token'))
    return None


def get_media_id(ACCESS_TOKEN, file):
    url = f'https://qyapi.weixin.qq.com/cgi-bin/media/upload?access_token={ACCESS_TOKEN}&type=image'
    m = MultipartEncoder(
        fields={'filename': ('test.png', open(file, 'rb'), 'image/png')},
    )
    headers = {
        'Content-Type': m.content_type
    }
    r = requests.post(url, data=m, headers=headers).json()
    if r.get('errmsg') != 'ok':
        raise
    return r.get('media_id')


def put_message(access_token,media_id):
    url = f'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={access_token}'
    data = {
        "touser": "@all",
        "toparty": "@all",
        "totag": "@all",
        "msgtype": "image",
        "agentid": 1000002,
        "image": {
            "media_id": media_id
        },
        "safe": 0,
        "enable_id_trans": 0,
        "enable_duplicate_check": 0,
        "duplicate_check_interval": 1800
    }
    r = requests.post(url, json=data).json()
    if r.get('errmsg') != 'ok':
        raise


def send():
    filename = 'result.png'
    try:
        access_token = open('access_token.txt', 'r', encoding='utf-8').read()
        media_id = get_media_id(access_token, filename)
        put_message(access_token,media_id)
    except:
        get_access_token()
        access_token = open('access_token.txt', 'r', encoding='utf-8').read()
        media_id = get_media_id(access_token, filename)
        put_message(access_token,media_id)

