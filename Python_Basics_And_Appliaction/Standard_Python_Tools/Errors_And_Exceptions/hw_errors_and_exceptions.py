error_parents = {}
error_sons = dict()
error_all = set()
used = set()

for _ in range(int(input())):
    error = input().split()
    error_all.add(error[0])
    error_parents[error[0]] = set() if len(error) == 1 else set(error[2:])
    if len(error) > 1:
        for tmp in error[2:]:
            error_all.add(tmp)

for key in error_all:
    error_sons[key] = set()

for key in error_parents.keys():
    for parent in error_parents[key]:
        error_sons[parent].add(key)


def set_used(current_parent):
    used.add(current_parent)
    if error_sons[current_parent] == set():
        return
    for son in error_sons[current_parent]:
        set_used(son)


ans = []

for _ in range(int(input())):
    error = input()
    if error in used:
        if error not in ans:
            ans.append(error)
    else:
        set_used(error)

for a in ans:
    print(a)
