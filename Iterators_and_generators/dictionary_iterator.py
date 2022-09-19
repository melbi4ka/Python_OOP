class dictionary_iter:

    def __init__(self, obj):
        self.obj = obj
        self.end = len(obj) - 1
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.end >= 0:
            items = list(self.obj.items())
            result = items[self.start]
            self.end -= 1
            self.start += 1
            return result
        raise StopIteration()


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
