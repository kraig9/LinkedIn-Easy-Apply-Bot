import requests

url = "http://localhost:11434/api/generate"
company = "Google"
question = "What is your experience with machine learning?"
data = {
    "model": "llama2",
    "prompt": "Act like you're applying to a senior machine learning engineer positions at " + company + " and keep your answer short and in paragraph form. \
    act like you have 5 years of experience and do not have any unfilled fields like [current company]. \
     Answer this question: " + question,
    "stream": False
}

response = requests.post(url, json=data)
# print(response.json())

print("Response is: " + response.json()['response'])