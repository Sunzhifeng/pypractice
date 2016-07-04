"""
    This is an example of decorator class, but it only decorate functions.
"""


class myDecorator(object):
    """ A class decorator used to decorate function.
    """
    def __init__(self, f):
        print 'myDecorator __init__'
        self.f = f

    def __call__(self, *args, **kwargs):
        print 'myDecorator __call__'
        self.f(*args, **kwargs)


@myDecorator
def hello(content):
    print 'hello %s' % content


def hello2(content):
    print 'hello2 %s' % content


hello('decorator')

# equal with @myDecorator
myDecorator(hello2)('decorator')
