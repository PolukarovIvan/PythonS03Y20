import sys
import re
import requests


# Task: There is 2 URLs: A and B. Output "Yes" if we can go from A to B via one url, else Output "No"
def find_b_from_a(arr_url):
    first_path = arr_url[0]
    second_path = arr_url[1]
    pattern = r'href="(.+?)"'

    first_request = requests.get(first_path)
    if first_request.status_code != 200:
        return False

    new_paths = re.findall(pattern, str(first_request.content))

    for pth in new_paths:
        current_request = requests.get(pth)
        if current_request.status_code == 200:
            if re.search(second_path, str(current_request.content)):
                return True

    return False


print("Yes" if find_b_from_a([input() for i in range(2)]) else "No")
