import json
import re

# with open("students.json", 'r') as f:
#     data = json.load(f)
#     print(data)
data = json.loads(input())
pattern = r'"parents": [(.+?)]'
d = {}
#print(re.findall(pattern, str(data)))
sons = {}

for i in range(len(data)):
    sons[data[i]["name"]] = set()
    for element in data[i]["parents"]:
        sons[element] = set()

for i in range(len(data)):
    for element in data[i]["parents"]:

        sons[element].add(data[i]["name"])

        for j in range(len(data)):
            son = data[i]["name"]
            if son in data[j]["parents"]:

                sons[element].add(data[j]["name"])

names = sorted(sons)

for name in names:
    print("{} : {}".format(name, len(sons[name]) + 1))


