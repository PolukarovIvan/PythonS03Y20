import os
import os.path

data = []
pth = "C:/Users/vanis/Desktop/main"
with open("ans.txt", "w") as ans:
    os.chdir(pth)
    for current_dir, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith(".py"):
                data.append(current_dir[2:])
                break
    data.sort()
    print(data)
    ans.write('\n'.join(data))
