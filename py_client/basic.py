import requests

endpoint = "http://localhost:8000"

get_response = requests.get(endpoint, json={"query": "Hello World"})

print(get_response)
# print(get_response.text)
# print(get_response.status_code)
