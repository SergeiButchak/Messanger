import inspect
from functools import wraps


def log(func):
    @wraps(func)
    def call(*args, **kwargs):
        if func.__code__.co_code == b'd\x00S\x00':
            upper_func = inspect.stack()[1][3]
            print(inspect.stack())
            print(f'{func.__name__} does nothing, called from {upper_func}')
        return func(*args, **kwargs)
    return call

@log
def my():
    pass


@log
def my1():
    print('Hello')


my()
my1()
