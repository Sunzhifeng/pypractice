"""  A function decorator with args
"""
import time


def outer_decorator(*outer_args, **outer_kwargs):
    """ a template of function decorator  with args
    """
    def decorator(func):
        def decorated(*args, **kwargs):
            print outer_args, outer_kwargs
            return func(*args, **kwargs)
        return decorated

    return decorator


def sleep(func):
    """ a sleep decorator to control the speed of function executing.
    """
    def wrapper(*args, **kwargs):
        print 'sleep...'
        time.sleep(2)
        return func(*args, **kwargs)

    return wrapper


def time_sleep(*outer_args, **outer_kwargs):
    """ a sleep decorator with args to control the speed of function executing.
    """
    def wrapper(func):
        def wrap(*args, **kwargs):
            print 'sleep...'
            time.sleep(*outer_args, **outer_kwargs)
            return func(*args, **kwargs)
        return wrap

    return wrapper


@sleep
def foo():
    print 'foo <@sleep>'


@time_sleep(5)
def foo2():
    print 'foo2 <@sleep(5)>'


def foo3():
    print 'foo3'


def main():
    foo()
    foo2()

    # the prototype of function decorator with args
    sleep(foo3)()
    time_sleep(5)(foo3)()


if __name__ == '__main__':
    main()
