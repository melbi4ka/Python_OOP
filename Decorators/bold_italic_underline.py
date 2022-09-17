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

