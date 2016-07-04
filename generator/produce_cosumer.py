#!/usr/bin/env python3


def consumer():
    r = 'YES'
    while True:
        print('[CONSUMER] Ready to consume')
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s ....' % n)
        r = '200 OK'


def producer(c):
    print('[PRODUCER] Are you ready ?')
    r = c.send(None)
    print('[PRODUCER] Consumer return %s ' % r)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s ...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return %s ...' % r)
    c.close()


def main():
    producer(consumer())


if __name__ == '__main__':
    main()
