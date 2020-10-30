import requests

res = requests.get("https://yandex.ru/search/", params={"text": "asd"})

print(res.status_code)
print(res.url)