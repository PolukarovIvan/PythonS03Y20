def fib(k):
    if k == 1 or k == 0:
        return 1
    else:
        return fib(k - 1) + fib(k - 2)


print(__name__)

print(fib(34))