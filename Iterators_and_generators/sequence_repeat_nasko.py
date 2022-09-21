class sequence_repeat:

    def __init__(self, sequence, count):
        self.sequence = sequence
        self.count = count
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count ==  self.idx:
            raise StopIteration
        result = self.sequence[self.idx % len(self.sequence)]
        self.idx += 1
        return result


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')

