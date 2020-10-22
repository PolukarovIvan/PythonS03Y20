from random import random


def simple_gen():
    print("Checkpoint 1")
    yield 1
    print("Checkpoint 2")
    yield 2
    print("Checkpoint 3")


print(type(simple_gen()))

gen = simple_gen()
x = next(gen)
print(x)
y = gen.__next__()
print(y)


def random_generator(size):
    for i in range(size):
        yield random()


for element in random_generator(10):
    print(element)
