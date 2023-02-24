import requests
import json


def post(query):
    url = 'http://127.0.0.1:8888'
    payload = {'query': query}
    response = requests.post(url=url, data=payload)
    return response.json()

def get(query):
    url = f'http://127.0.0.1:8888/?query={query}'
    response = requests.get(url)
    return response.json()

print(post('hi'))