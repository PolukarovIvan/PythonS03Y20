import operator as op
import itertools

a, b = 4, 5

# some simple operations
print(op.add(a, b))
print(op.mul(a, b))
print(op.mul([3], 3))

# methodcaller
alist = ["wolf", "ship", "duck"]
print(list(filter(lambda x: x.startswith('d'), alist)))  # keep only elements that start with 'd'
print(list(filter(op.methodcaller('startswith', 'd'), alist)))  # does the same but is faster
# Output: ['duck']

# itemgetter
x = [1, 2, 3]
f1 = op.itemgetter(1)  # returns function f(x), that returns element with index 1
print(f1(x))  # Output: 2

d = {"123": 1, "aba": 2}
f2 = op.itemgetter("123")
print(f2(d))

# attergetter
f3 = op.attrgetter("sort")  # f(x) == x.sort()
print(f3([3, 2, 1]))

x = [
    ("Guido", "Van", "Rossum"),
    ("Edward", "Baker"),
    ("El", "Pacito", "Hurban")
]

x.sort(key=op.itemgetter(-1))
print(x)