import requests

res = requests.get(
    "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/SVG-edit_logo.svg/1200px-SVG-edit_logo.svg.png")
print(res.status_code)
print(res.headers["Content-Type"])

with open("logo.png", "wb") as logo:
    logo.write(res.content)
