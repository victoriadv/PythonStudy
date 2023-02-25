import requests

res = requests.get("https://google.com")

if res:
    print('Response OK')
else:
    print('Response Failed')

print(res.text)