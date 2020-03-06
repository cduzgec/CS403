import requests

API_URL = 'http://127.0.0.1:5000'

response = requests.get(API_URL)
if response.ok:
    result = response.json()  #200 is response code
    secret = result['secret']
    print(secret)
