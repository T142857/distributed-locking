# queue_lifo.py
"""
LifoQueue uses last-in, first-out ordering ~ a stack data structure
"""
import queue

q = queue.LifoQueue()

for i in range(5):
    q.put(i)

while not q.empty():
    print(q.get(), end=' ')
print()
