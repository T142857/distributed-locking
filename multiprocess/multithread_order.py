#!/usr/bin/env python3

import threading
import time
import random


def hello(n):
    time.sleep(random.randint(1, 3))
    print("[{0}] Hello!".format(n))


threads = []
for i in range(10):
    t = threading.Thread(target=hello, args=(i,))
    threads.append(t)
    t.start()

for one_thread in threads:
    one_thread.join()

print("Done!")

"""
if you want to be sure that "Done!"
is printed after all the threads have finished running, you can use join
...
./multithread_order.py
[2] Hello!
[8] Hello!
[7] Hello!
[4] Hello!
[5] Hello!
[0] Hello!
[6] Hello!
[1] Hello!
[9] Hello!
[3] Hello!
Done!
"""
