import requests
u=requests.get('http://127.0.0.1:12345/json')
#print(u.text)
print(u.json())

