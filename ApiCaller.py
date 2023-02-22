import requests

with open('NgrokServerUrl.txt', 'r') as f:
    url = f.read()

response = requests.get(f"{url}")
print(response.json())