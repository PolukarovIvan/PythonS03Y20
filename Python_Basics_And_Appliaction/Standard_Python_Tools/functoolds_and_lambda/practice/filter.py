# Filter
def is_even(x):
    return x % 2 == 0


lst = list(map(int, input().split()))
filter_obj1 = filter(is_even, lst)
print(filter_obj1)
print(list(filter_obj1))
print(list(filter_obj1))

filter_obj2 = filter(is_even, lst)

while True:
    try:
        print(next(filter_obj2), end = " ")
    except StopIteration as e:
        print()
        print(e.__doc__)
        break
