#!/usr/bin/env python3

import multiprocessing
import time
import random
import os
from multiprocessing import Queue

q = Queue()


def hello(n):
    time.sleep(random.randint(1, 3))
    q.put(os.getpid())
    print("[{0}] Hello!".format(n))


processes = []
for i in range(10):
    t = multiprocessing.Process(target=hello, args=(i, ))
    processes.append(t)
    t.start()

for one_process in processes:
    one_process.join()

my_list = []
while not q.empty():
    my_list.append(q.get())

print("Done!")
print(len(my_list))
print(my_list)

"""
queues in the world of multithreaded programs prevent issues having to do with thread safety. But in the world of multiprocessing, queues allow you to bridge the gap among your processes, sending data back to the main process.
./multiprocess_queue.py
[3] Hello!
[7] Hello!
[9] Hello!
[6] Hello!
[0] Hello!
[2] Hello!
[1] Hello!
[5] Hello!
[4] Hello!
[8] Hello!
Done!
10
[17780, 17784, 17786, 17783, 17777, 17779, 17778, 17782, 17781, 17785]

Process finished with exit code 0
"""
