def fibonacci():
    start = 0
    second = 1
    yield start
    yield second

    while True:

        result = start + second
        start, second = second, result
        yield result


generator = fibonacci()
for i in range(5):
    print(next(generator))
