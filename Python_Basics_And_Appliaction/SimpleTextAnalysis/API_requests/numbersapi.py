import json
import requests
import re
import sys

pth = "http://numbersapi.com"
params = {"json": "true"}

with open("C:/Users/vanis/Downloads/dataset_24476_3.txt", 'r') as f:
    data = f.read().split()

print(data)
# print(requests.get(pth).status_code)
with open("ans.txt", "w") as f:
    for number in data:
        new_pth = pth + "/" + number + "/math"
        res = requests.get(new_pth, params=params)
        # print(res.text)
        # print(res.headers["Content-type"])
        data = res.json()
        # print(data)
        f.write("Interesting\n" if data["found"] else "Boring\n")
