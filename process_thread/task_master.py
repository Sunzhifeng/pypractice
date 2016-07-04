#!/usr/bin/env python3

""" simulating distributed processes, eg, master/worker
"""

import time
import queue
import random
from multiprocessing.managers import BaseManager


task_queue = queue.Queue()
result_queue = queue.Queue()


class QueueManager(BaseManager):
    pass


QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)

manager =QueueManager(address=('', 5000), authkey=b'abc')

manager.start()

task = manager.get_task_queue()
result = manager.get_result_queue()

# put some tasks
for i in range(10):
    n = random.randint(0, 10000)
    print('Put task %d...' % n)
    task.put(n)

# get results
print('Trying get results...')
for i in range(10):
    n = result.get(timeout=10)
    print('Result: %s' % n)

manager.shutdown()
print('master exit.')
