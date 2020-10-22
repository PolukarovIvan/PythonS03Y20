def foo(a, b):
    return a + b


def returned_mas():
    return 1, 2


print(foo(*returned_mas()))
