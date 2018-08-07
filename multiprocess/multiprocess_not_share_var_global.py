#!/usr/bin/env python3


import multiprocessing
import time
import random
import os

# variable global
my_list = []


def hello(n):
    time.sleep(random.randint(1, 3))
    my_list.append(os.getpid())
    print("[{0}] Hello!".format(n))


processes = []
for i in range(10):
    t = multiprocessing.Process(target=hello, args=(i,))
    processes.append(t)
    t.start()

for one_process in processes:
    one_process.join()

print("Done!")
print(len(my_list))
print(my_list)

"""
Each time it creates a new process with "multiprocessing", 
each process has its own value of the global mylist list. 
Each process thus adds to its own list, which goes away when the processes are joined.
./multiprocess_not_share_var_global.py
[0] Hello!
[7] Hello!
[9] Hello!
[2] Hello!
[4] Hello!
[6] Hello!
[5] Hello!
[8] Hello!
[1] Hello!
[3] Hello!
Done!
0
[]

Process finished with exit code 0
"""
