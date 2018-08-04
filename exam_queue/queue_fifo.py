"""
FIFO Queue class implements a basic first-in, first-out collections.
- put() method: add item the end of queue
- get() method: remove item the head of queue
"""
import queue

q = queue.Queue()

for i in range(5):
    q.put(i)

while not q.empty():
    print(q.get(), end=' ')
print()
