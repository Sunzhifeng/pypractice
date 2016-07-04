#!/usr/bin/env python

"""
    An example for computing fib number
"""


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1


def main():
    for n in fib(6):
        print n


if __name__ == '__main__':
    main()
