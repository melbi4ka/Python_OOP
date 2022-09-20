from itertools import permutations

def possible_permutations(iterable):

    for el in permutations(iterable):
        yield list(el)


[print(n) for n in possible_permutations([1, 2, 3])]
