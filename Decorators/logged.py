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

# @logged
# def sum_func(a, b):
#     return a + b
# print(sum_func(1, 4))


# искаме да принтираме резултата на функцията съм функ, както и да изкараме аргументите, които се подават
# функцията прави различни неща според входа - събира аргументите, събира 3 с дължината на листа и пр.
# декорираме я с декоратор - логед
# на функцията логед - подаваме функцията съм фънк
# логед извиква рапър - с аргументите
# правим първия ред на резултата според изискването на задачите
# във втория ред правим ф-стринг, който извиква функцията и подава разопакованите аргументи
# функцията ще слезе във фънк и ще изчисли
# връщаме резултата
# връщаме референция към функцията



# test zero
import unittest

class LoggedTests(unittest.TestCase):
    def test_zero(self):
        @logged
        def func(*args):
            return 3 + len(args)
        result = func(4, 4, 4)
        self.assertEqual(result, 'you called func(4, 4, 4)\nit returned 6')

if __name__ == '__main__':
    unittest.main()