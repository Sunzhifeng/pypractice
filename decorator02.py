"""
    This module is used to show some useful decorator example
"""

import time


def timing(func):

    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print '<%s> took %s to run' % (func.__name__, str(end - start))

    return wrapper


def sleep(func):

    def wrapper(*args, **kwargs):
        time.sleep(2)
        return func(*args, **kwargs)

    return wrapper


def timing_all_class_method(Cls):
    class NewCls(object):
        def __init__(self, *args, **kwargs):
            self.obj = Cls(*args, **kwargs)

        def __getattribute__(self, s):
            try:
                x = super(NewCls, self).__getattribute__(s)
            except AttributeError:
                pass
            else:
                return x

            x = self.obj.__getattribute__(s)
            if type(x) == type(self.__init__):    # x is instance method
                return timing(x)
            else:
                return x

    return NewCls


@timing
def hello(content):
    print 'hello %s' % content


@timing_all_class_method
class Foo(object):
    def hello(self, content):
        print 'Foo:hello %s' % content


if __name__ == '__main__':

    hello('world')
    foo = Foo()
    foo.hello('world')
