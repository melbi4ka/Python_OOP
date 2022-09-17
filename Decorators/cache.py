from functools import wraps


def cache(func):
    memo = {}

    @wraps(func)
    def wrapper(n):
        if n in memo:
            return memo[n]
        res = func(n)
        memo[n] = res
        return res

    wrapper.log = memo
    return wrapper

@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(8))
print(fibonacci.log)
