#!/usr/bin/env python3

""" simulating distributed processes, eg, master/worker
"""

import time
from multiprocessing.managers import BaseManager


class QueueManager(BaseManager):
    pass


# get queue from net and only give the name
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

server_addr = '127.0.0.1'
print('Connect to server: %s ...' % server_addr)

manager = QueueManager(address=(server_addr, 5000), authkey=b'abc')

manager.connect()

task = manager.get_task_queue()
result = manager.get_result_queue()

# get task from task-queue, and put result into result-queue
for i in range(10):
    try:
        n = task.get(timeout=1)
        print ('run task %d * %d ...' % (n, n))
        r = '%d * %d = %d' % (n, n, n*n)
        time.sleep(1)
        result.put(r)
    except queue.Empty:
        print('task queue is empty.')

print('worker exit.')
