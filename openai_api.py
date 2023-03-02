import openai

api_key = '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'
openai.api_key = api_key

result = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "请问你有没有感情"}
    ]
)
tokens = result['usage']['total_tokens']
respond = result['choices'][0]['message']['content']
print(respond)

result = {
    "choices": [
        {
        "finish_reason": "stop",
        "index": 0,
        "message": {
            "content": "作为一台计算机程序，我没有情感和感情。我只是根据预定的算法和程序执行任务。",
            "role": "assistant"
        }
        }
    ],
    "created": 1677734774,
    "id": "chatcmpl-6pVkE9lgzAg2stgISaTyb6mMCYVfs",
    "model": "gpt-3.5-turbo-0301",
    "object": "chat.completion",
    "usage": {
        "completion_tokens": 35,
        "prompt_tokens": 14,
        "total_tokens": 49
    }
}