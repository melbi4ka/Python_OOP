def get_primes(iterable):

    for num in iterable:
        if num > 1:
            if all(num % i != 0 for i in range(2, num)):
                yield num



print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))