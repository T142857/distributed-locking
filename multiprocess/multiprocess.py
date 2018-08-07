#!/usr/bin/env python3

import multiprocessing
import time
import random


def hello(n):
    time.sleep(random.randint(1, 3))
    print("[{0}] Hello!".format(n))


processes = []
for i in range(10):
    t = multiprocessing.Process(target=hello, args=(i,))
    processes.append(t)
    t.start()

for one_process in processes:
    one_process.join()

print("Done!")

"""
./multiprocess.py

[4] Hello!
[0] Hello!
[2] Hello!
[9] Hello!
[1] Hello!
[3] Hello!
[7] Hello!
[6] Hello!
[8] Hello!
[5] Hello!
Done!
"""
