# lambda - function usages

# # bad usage:
# a, b = map(int, input().split())
# foo = lambda x, y: x ** 2 + y ** 2
# print(foo(a, b))

# normal usage:
data = list(map(int, input().split()))
even_data = list(filter(lambda x: x % 2 == 0, data))
print(data)
print(even_data)

# sorting with lambda:

# sorting depending on worlds' length

names = ["Ivan", "Liza", "Abraham", "13", "Ali"]
print(names)
names.sort()
print(names)
names.sort(key=lambda x: len(x))
print(names)

x = [
    ("Guido", "Van", "Rossum"),
    ("Muhamed", "Ali"),
    ("Abraham", "A")
]

print(x)
x.sort(key=lambda x: len(x))
print(x)
print([len(element) for element in x])

# sorting with full name length:
x.sort(key=lambda name: len(" ".join(name)))
print(x)
print([len(" ".join(name)) for name in x])
