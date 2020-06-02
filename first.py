import requests
import json

url = 'https://reqres.in/api/users?page=2'

response = requests.get(url)

print(response)

json_response = json.loads(response.text)
print('-------')
print(json_response)