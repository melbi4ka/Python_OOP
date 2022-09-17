from functools import wraps


def tags(param):

    def decorator(function):

        @wraps(function)
        def wrapper(*args):
            res = function(*args)
            result = f"<{param}>{res}</{param}>"
            return result

        return wrapper

    return decorator



@tags('p')
def join_strings(*args):
    return "".join(args)
print(join_strings("Hello", " you!"))

@tags('h1')
def to_upper(text):
    return text.upper()
print(to_upper('hello'))


# test first zero
import unittest

class TagsTests(unittest.TestCase):
    def test_zero_first(self):
        @tags('p')
        def join_strings(*args):
            return "".join(args)
        self.assertEqual(join_strings("Hello", " you!"), '<p>Hello you!</p>')

if __name__ == '__main__':
    unittest.main()