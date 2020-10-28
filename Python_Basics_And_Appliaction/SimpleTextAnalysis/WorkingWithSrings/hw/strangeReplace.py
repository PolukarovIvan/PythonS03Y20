def how_many(s, a, b):
    if a not in s:
        return 0

    if a in b:
        return "Impossible"

    counter = 0

    while a in s:
        s = s.replace(a, b)
        counter += 1

    return counter


s = input()
a = input()
b = input()

print(how_many(s, a, b))
