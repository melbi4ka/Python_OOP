class sequence_repeat:

    def __init__(self, sequence, count):
        self.sequence = sequence
        self.count = count
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count > 0:
            if self.start == len(self.sequence):
                self.start = 0
            result = self.sequence[self.start]
            self.start += 1
            self.count -= 1
            return result
        raise StopIteration()


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')


