import requests
import json

with open("dataset_24476_4.txt", "r") as f:
    data = f.read().split()

print(data)

client_id = "201bb76dd94cdcb00cd3"
client_secret = "90ac67b7cbecc5257f0198945392e37b"

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)

# достаем токен
token = j["token"]

# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token": token}
# инициируем запрос с заголовком
pth = "https://api.artsy.net/api/artists/"

with open("artists_ans.txt", "w", encoding="utf-8") as f:
    res = []

    for author_id in data:
        cur_pth = pth + author_id
        r = requests.get(cur_pth, headers=headers)
        r.encoding = 'utf-8'
        j = json.loads(r.text)

        res.append({"birth": j["birthday"], "name": j["sortable_name"]})
        # print(repr(j["name"]))
    print(res)
    res.sort(key=lambda x: (x["birth"], x["name"]))
    print(res)

    for artist in res:
        #a = artist["name"].split()
        f.write(artist["name"] + "\n")
        print(artist["name"])

