"""
Here's a simple example of how a function running in a thread can modify a global variable
(note that what I'm doing here is to prove a point;
if you really want to modify global variables from within a thread,
you should use a lock)
"""

# !/usr/bin/env python3

import threading
import time
import random

# variable global
my_list = []


def hello(n):
    time.sleep(random.randint(1, 3))
    my_list.append(threading.get_ident())   # bad in real code
    print("[{0}] Hello!".format(n))


threads = []
for i in range(10):
    t = threading.Thread(target=hello, args=(i, ))
    threads.append(t)
    t.start()

for one_thread in threads:
    one_thread.join()

print("Done!")
print(len(my_list))
print(my_list)

"""
So, you can see that the global variable mylist is shared by the threads, and that when one thread modifies the list,
that change is visible to all the other threads. 
./multithread_share_var_global.py
[2] Hello!
[5] Hello!
[7] Hello!
[9] Hello!
[1] Hello!
[4] Hello!
[6] Hello!
[0] Hello!
[3] Hello!
[8] Hello!
Done!
10
[140250716862208, 140250691684096, 140250336716544, 140250319931136, 140250725254912, 140250700076800, 140250345109248, 140250733647616, 140250708469504, 140250328323840]
"""
