class countdown_iterator:

    def __init__(self, end):
        self.end = end
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.end >= self.start:
            current = self.end
            self.end -= 1
            return current
        raise StopIteration()



iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")
