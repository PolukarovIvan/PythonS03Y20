from random import random


class RandomIterator:
    def __init__(self, size):
        self.size = size
        self.counter = 0

    def __next__(self):
        if self.counter < self.size:
            self.counter += 1
            return random()
        else:
            raise StopIteration

    def __iter__(self):
        return self


x = RandomIterator(4)

for x in RandomIterator(10):
    print(x)