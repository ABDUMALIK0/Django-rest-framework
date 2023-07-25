import requests

# REST API -> Web API
#endpoint = 'https://httpbin.org/anything'
endpoint = 'http://localhost:8000/api/' # http://127.0.0.1:8000/


get_response = requests.post(endpoint, json={'title':"hello world"})#params={'abc':123},
#print(get_response.text)
#print(get_response.status_code)

print(get_response.json())