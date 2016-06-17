"""
    This is an example of decorator class
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


class Foo(object):
    def __init(self, name):
        print 'Foo __init__'
        self.name = name

    @myDecorator
    def say(self, content):
        print 'say %s' % content

    def __call__(self, *args, **kwargs):
        print 'Foo __call__'


@myDecorator
def hello(content):
    print 'hello %s' % content


hello('decorator')

foo = Foo('foo')
foo.say('decorator')

