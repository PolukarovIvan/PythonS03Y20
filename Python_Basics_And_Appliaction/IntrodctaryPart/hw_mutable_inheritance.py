base = {}


def test(parent, child):
    if parent == child or parent in base[child]:
        return True
    for current in base[child]:
        if test(parent, current):
            return True
    return False


n_classes = int(input())
base = {}

for i in range(n_classes):
    tmp_com = input().split()
    base[tmp_com[0]] = [] if len(tmp_com) == 1 else tmp_com[2:]

n_requests = int(input())

for i in range(n_requests):
    child, parent = input().split()
    print("Yes" if test(parent, child) else "No")