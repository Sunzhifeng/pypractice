#!/usr/bin/env python

"""
    An example for context manager
"""
class ContextManager(object):
    def __init__(self):
        print 'init'

    def __enter__(self):
        print 'enter'
        return self

    def __exit__(self, type, value, traceback):
        print 'exit'

    def say(self, content):
        print 'Hello %s' % content


def main():
    with  ContextManager() as cm:
        cm.say('ContextMangeer')

if __name__ == '__main__':
    main()
