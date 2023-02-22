import requests

response = requests.get("http://ffe3-168-5-42-254.ngrok.io/user/?user=sdjfio")
print(response.json())