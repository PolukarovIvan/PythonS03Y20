class DoubleElementListIterator(list):
    def __init__(self, lst):
        self.lst = lst
        self.size = 0

    def __next__(self):
        if self.size + 2 <= len(self.lst):
            self.size += 2
            return self.lst[self.size - 1], self.lst[self.size - 2]
        else:
            raise StopIteration


class MyList(list):
    def __iter__(self):
        return DoubleElementListIterator(self)


for pair in MyList([1, 2, 3, 5]):
    print(pair)
