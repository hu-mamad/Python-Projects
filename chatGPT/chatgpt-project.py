import requests

api_enpoint = "https://api.openai.com/v1/completions"
api_key = "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"
request_headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer" + api_enpoint
}

request_data = {
    "model": "text-davinci-003",
    "prompt": "what Time is it: ",
    "max_tokens": 100,
    "temperature": 0.5
}

response = requests.post(api_enpoint, headers=request_headers, json=request_data)

if response.status_code == 200:
    print(response.json())
else:
    print(f"Request failed with status code: {str(response.status_code)}")