import requests

api_enpoint = "https://api.openai.com/v1/completions"
api_key = "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"
request_headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer" + api_key
}

request_data = {
    "model": "text-davinci-003",
    "prompt": "what Time is it: ",
    "max_tokens": 100,
    "temperature": 0.5
}

response = requests.post(api_enpoint, headers=request_headers, json=request_data)

print(response.json())    