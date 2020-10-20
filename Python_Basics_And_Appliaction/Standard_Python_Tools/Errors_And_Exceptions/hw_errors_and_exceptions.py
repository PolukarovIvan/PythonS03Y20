errors = {}

n_errors = int(input())

for _ in range(n_errors):
    tmp_error = input().split()
    if len(tmp_error) == 1:
        errors[tmp_error[0]] = set()
    else:
        for element in tmp_error[2:]:
            if not element in errors.keys():
                errors[element] = set()
            errors[element].add(tmp_error[0])
            errors[tmp_error[0]] = set()


def set_used(some_error):
    used.add(some_error)
    for current_error in errors[some_error]:
        set_used(current_error)


n_commands = int(input())
used = set()
ans = list()

for _ in range(n_commands):
    error = input()
    if error in used:
        if not error in ans:
            ans.append(error)

    else:
        set_used(error)

for answer in ans:
    print(answer)

