"""
    A funcion decorator to decorate instance method.
"""

import time


def timing(func):
    """ a timing decorator is used to count function running time.
    """
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print '<%s> took %s to run' % (func.__name__, str(end - start))

    return wrapper


class Foo(object):
    def __init__(self, name):
        print 'Foo __init__'
        self.name = name

    @timing
    def say(self, content):
        print 'say %s' % content

    def __call__(self, *args, **kwargs):
        print 'Foo __call__'


foo = Foo('foo')
foo.say('decorator')
