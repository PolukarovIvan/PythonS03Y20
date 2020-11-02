import re
import requests

# pth = "http://pastebin.com/raw/7543p0ns"
file = requests.get(input())
# print(file.status_code)
pattern1 = r'(https?://[\w.-]+)'
pattern2 = r"://([A-Za-z0-9-.]+)"
ans = sorted(set(re.findall(pattern1, str(file.content))))
s = ' '.join(ans)
print(s)
ans = sorted(set(re.findall(pattern2, s)))
print("\n".join(ans))
