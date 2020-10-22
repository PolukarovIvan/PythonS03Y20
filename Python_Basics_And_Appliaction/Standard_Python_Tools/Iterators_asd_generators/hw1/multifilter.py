class multifilter:
    def judge_half(self, pos, neg):
        return pos >= neg

    def judge_all(self, pos, neg):
        return neg == 0

    def judge_any(self, pos, neg):
        return pos >= 1

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable = iterable
        self.funcs = funcs
        self.judge = judge
        self.index = 0

    def res_count(self, a):
        res = [f(a) for f in self.funcs]
        return res.count(True), res.count(False)

    def __iter__(self):
        for element in self.iterable:
            neg = 0
            pos = 0
            # print(self.res_count(element))
            pos, neg = self.res_count(element)
            if self.judge(self, pos, neg):
                yield element
            pos = 0
            neg = 0


def mul2(x):
    return x % 2 == 0


def mul3(x):
    return x % 3 == 0


def mul5(x):
    return x % 5 == 0


a = [i for i in range(31)]  # [0, 1, 2, ... , 30]

print(list(multifilter(a, mul2, mul3, mul5)))

print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half)))
# [0, 6, 10, 12, 15, 18, 20, 24, 30]

print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all)))
# [0, 30]