import itertools


def primes():
    # infinity primes_numbers generator using Wilson's Th.
    i, f = 2, 1  # The number and factorial(number - 1)
    while True:  # Infinity cycle
        if (f + 1) % i == 0:  # Wilson's Th.
            yield i
        f, i = f * i, i + 1  # Recalculation of the factorial and i


print(list(itertools.takewhile(lambda x: x <= 31, primes())))
