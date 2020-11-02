import json

data = [{"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}, {"name": "A", "parents": []},
        {"name": "D", "parents": ["C", "F"]}, {"name": "E", "parents": ["D"]}, {"name": "F", "parents": []}]

print(json.dumps(data, indent=4, sort_keys=True))

with open("students.json", 'w') as f:
    json.dump(data, f, indent=4, sort_keys=True)
