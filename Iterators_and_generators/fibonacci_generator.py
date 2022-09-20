def fibonacci():
    start = 0
    second = 1
    while True:
        yield start
        result = start + second
        start = second
        second = result



generator = fibonacci()
for i in range(5):
    print(next(generator))
