import hashlib
import requests

appid = '20230223001572583'
key = 'LbGJ114ECr7RhvK5dS5J'
salt = '1435660288'

def translate(text , from_language = 'auto' , to_language = 'zh'):
    sign = hashlib.md5(f'{appid}{text}{salt}{key}'.encode('utf-8')).hexdigest()
    url = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
    url += f'?q={text}&from={from_language}&to={to_language}&appid={appid}&salt={salt}&sign={sign}'
    try:
        return requests.get(url).json()['trans_result'][0]['dst']
    except Exception:
        return None

def language_detect(text):
    sign = hashlib.md5(f'{appid}{text}{salt}{key}'.encode('utf-8')).hexdigest()
    url = 'https://fanyi-api.baidu.com/api/trans/vip/language'
    url += f'?q={text}&salt={salt}&sign={sign}&appid={appid}'
    try:
        return requests.get(url).json()['data']['src']
    except Exception:
        return None

if __name__ == "__main__":
    print(language_detect('注意：在使用本方法之前，需要先安装 requests 库和 hashlib 库。'))