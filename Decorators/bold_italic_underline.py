from functools import wraps


def make_bold(function):

    @wraps(function)
    def wrapper(*args, **kwargs):
        result = f"<b>{function(*args, **kwargs)}</b>"
        return result

    return wrapper

def make_italic(function):

    @wraps(function)
    def wrapper(*args, **kwargs):
        result = f"<i>{function(*args, **kwargs)}</i>"
        return result

    return wrapper

def make_underline(function):

    @wraps(function)
    def wrapper(*args, **kwargs):
        result = f"<u>{function(*args, **kwargs)}</u>"
        return result

    return wrapper


@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"

print(greet("Peter"))
# @make_bold
# @make_italic
# @make_underline
# def greet_all(*args):
#     return f"Hello, {', '.join(args)}"
#
# print(greet_all("Peter", "George"))

# имаме функция гриит, която декорираме с три декоратора
# т.е правим три отделни декоратора във функции
# стандартни декоратори - на декоратора подаваме функцията
# за да не достъпваме рапъра, а нещата на основната функция - декорираме рапъра с
#  рапс от фънктулс
# рапса вътре работи с аргс
# пишем си бизнес логиката
# връщаме резултат 


import unittest


class BoldItalicUnderlineTests(unittest.TestCase):
    def test_make_bold(self):
        @make_bold
        def func():
            return "pesho"

        res = func()
        self.assertEqual(res, "<b>pesho</b>")

    def test_make_italic(self):
        @make_italic
        def func(name):
            return f"Hey, {name}"

        res = func("pesho")
        self.assertEqual(res, "<i>Hey, pesho</i>")

    def test_make_underline(self):
        @make_underline
        def func(first_name, last_name):
            return f"{first_name} {last_name}"

        res = func("pesho", "peshov")
        self.assertEqual(res, "<u>pesho peshov</u>")

    def test(self):
        @make_bold
        @make_underline
        @make_italic
        def func():
            return "pesho"

        res = func()
        self.assertEqual(res, "<b><u><i>pesho</i></u></b>")


if __name__ == "__main__":
    unittest.main()
