#!/usr/bin/env python3

import time
import threading


def say(content):
    print('The thread %s is running' % threading.current_thread().name)
    print('Say %s' % content)
    time.sleep(1)
    print('The thread %s end' % threading.current_thread().name)


if __name__ == '__main__':
    print('Thread %s is running' % threading.current_thread().name)

    t = threading.Thread(target=say, name='SayThread', args=('hello',))
    t.start()
    t.join()
    print('Thread %s end' % threading.current_thread().name)
