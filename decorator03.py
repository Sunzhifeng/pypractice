""" decorator with args
"""

def outer_decorator(*outer_args, **outer_kwargs):
    def decorator(func):
        def decorated(*args, **kwargs):
            print outer_args, outer_kwargs
            return func(*args, **kwargs)
        return decorated
    return decorator


@outer_decorator(1, 2, 3)
def foo(a, b, c):
    print a
    print b
    print c


def foo2(a, b, c):
    print a
    print b
    print c


foo('a', 'b', 'c')

outer_decorator(1, 2, 3)(foo2)('a', 'b', 'c')
