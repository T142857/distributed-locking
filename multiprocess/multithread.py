#!/usr/bin/env python3

import threading
import time
import random


def hello(n):
    time.sleep(random.randint(1, 3))
    print("[{0}] Hello!".format(n))


for i in range(10):
    threading.Thread(target=hello, args=(i,)).start()

print("Done!")

"""
the threads are running parallel, but not ORDER
...>Done!
[7] Hello!
[8] Hello!
[4] Hello!
[3] Hello!
[0] Hello!
[2] Hello!
[1] Hello!
[9] Hello!
[5] Hello!
[6] Hello!
"""
