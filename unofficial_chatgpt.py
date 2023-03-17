import os , sys , openai , contextlib , json , requests
import translate_baiduapi
import re

api_key = os.environ['OPENAI_API_KEY']

def respond(text):
    header = {
        'Authorization' : f'Bearer {api_key}',
        'Content-Type' : 'application/json'
    }
    data = {
        'model' : 'gpt-3.5-turbo',
        'messages' : [{'role' : 'user' , 'content' : text}]
    }
    try:
        # a = requests.post('https://visitcjc.top/v1/chat/completions' , headers = header , json = data).json()
        a = requests.post('https://chatgpt-api.shn.hk/v1/' , headers = header , json = data).json()
    except requests.exceptions.ConnectTimeout:
        return 0 , 0 , '由于连接方在一段时间后没有正确答复或连接的主机没有反应,连接尝试失败,请重试.'
    try:
        error = a['error']
        return error
    except KeyError:
        prompt_tokens = a['usage']['prompt_tokens']
        completion_tokens = a['usage']['completion_tokens']
        respond = a['choices'][0]['message']['content']
        return prompt_tokens , completion_tokens , respond

def check_billing():
    header = {
        'Authorization' : f'Bearer {api_key}'
    }
    a = requests.get('https://visitcjc.top/dashboard/billing/credit_grants' , headers = header).json()
    total_granted = a['total_granted']
    total_used = a['total_used']
    total_available = a['total_available']
    return total_granted , total_used , total_available

def respond_stream(text):
    response = openai.ChatCompletion.create(        
        model = 'gpt-3.5-turbo',
        messages = [{'role' : 'user', 'content' : text}],
        stream = True
    )
    for i in response:
        with contextlib.suppress(Exception):
            print(i['choices'][0]['delta']['content'] , end = '')
    print()

def respond_stream_post(text):
    header = {
        'Authorization' : f'Bearer {api_key}',
        'Content-Type' : 'application/json'
    }
    data = {
        'model' : 'gpt-3.5-turbo',
        'messages' : [{'role' : 'user' , 'content' : text}]
    }
    try:
        a = requests.post('https://chatgpt-api.shn.hk/v1/' , headers = header , json = data , stream = True)
        for line in a.iter_lines():
            if not line:
                continue
            decoded_line = line.decode('utf-8')
            yield json.loads(decoded_line)
    except requests.exceptions.ConnectTimeout:
        return 0 , 0 , '由于连接方在一段时间后没有正确答复或连接的主机没有反应,连接尝试失败,请重试.'
    try:
        error = a['error']
        return error
    except KeyError:
        prompt_tokens = a['usage']['prompt_tokens']
        completion_tokens = a['usage']['completion_tokens']
        respond = a['choices'][0]['message']['content']
        return prompt_tokens , completion_tokens , respond

def respond_stream_post_test(text):
    header = {
        'Authorization' : f'Bearer {api_key}',
        'Content-Type' : 'application/json'
    }
    data = {
        'model' : 'gpt-3.5-turbo',
        'messages' : [{'role' : 'user' , 'content' : text}],
        'stream' : True
    }
    response = requests.post('https://chatgpt-api.shn.hk/v1/' , headers = header , json = data , stream = True)
    full_respond = ''
    for line in response.iter_lines():
        if line != b'':
            a = line.decode('utf-8').split(':' , 1)[1].strip()
            with contextlib.suppress(Exception):
                a = json.loads(a)
                content = a['choices'][0]['delta']['content']
                if content != '\n\n':
                    print(content , end = '')
                    full_respond += content
    print()
    full_respond = full_respond.replace('\n' , '')
    full_respond = re.sub(r'(```.*?```)' , '******' , full_respond)
    language = translate_baiduapi.language_detect(full_respond)
    if language != 'zh':
        translate = translate_baiduapi.translate(full_respond).replace('。' , '.')
        print(f'\n{translate}')

while True:
    ask = input('Ask ChatGPT:')
    if ask == 'exit':
        sys.exit(0)
    print('ChatGPT:' , end = '')
    respond_stream_post_test(ask)