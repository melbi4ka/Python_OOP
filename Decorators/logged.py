def logged(function):

    def wraper (*args):

        # result = f"you called {function.__name__}({', '.join([str(arg)for arg in args])})"+"\n"
        result = f"you called {function.__name__}{args}"+"\n"
        result += f"it returned {function(*args)}"
        return result

    return wraper


@logged
def func(*args):
    return 3 + len(args)
print(func(4, 4, 4))

@logged
def sum_func(a, b):
    return a + b
print(sum_func(1, 4))

