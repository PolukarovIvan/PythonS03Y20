from functools import partial
import operator as op

x = int("1001", base=2)
print(x)

int_2 = partial(int, base=2)
print(int_2('1001'))

sort_by_last = partial(list.sort, key=op.itemgetter(-1))

x = [
    ("Guido", "Van", "Rossum"),
    ("Edward", "Baker"),
    ("El", "Pacito", "Hurban")
]

sort_by_last(x)
print(x)

y = ["abc", "cba", "abb"]
sort_by_last(y)
print(y)