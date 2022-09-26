class take_skip:

    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.iteration = 0

    def __iter__(self):
        return self

    def __next__(self):

        while self.count > 0:
            if self.iteration == self.count:
                raise StopIteration

            result = self.iteration * self.step
            self.iteration += 1
            return result


numbers = take_skip(2, 6)
for number in numbers:
    print(number)

numbers = take_skip(10, 5)
for number in numbers:
    print(number)
    
