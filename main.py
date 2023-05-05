import requests
import json

API_KEY = "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"
API_ENDPOINT = "https://api.openai.com/v1/chat/completions"

def generate_chat_completion(messages, model="gpt-3.5-turbo", temperature=1, max_tokens=None):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}",
    }

    data = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
    }

    if max_tokens is not None:
        data["max_tokens"] = max_tokens

    response = requests.post(API_ENDPOINT, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        raise Exception(f"Error {response.status_code}: {response.text}")
    
print("What can I help you with?: ")
while True:
    user_input = input("")
    messages = [
        {"role": "system", "content": "You are a bot is created to respond to text messages. Keep conversation with the user and remember previous responses."},
        {"role": "user", "content": user_input }
    ]

    response_text = generate_chat_completion(messages)
    print(response_text)