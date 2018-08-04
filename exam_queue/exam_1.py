"""
FIFO Queue class implements a basic first-in, first-out collections.
- put() method: add item the end of queue
- get() method: remove item the head of queue
"""
from queue import Queue


q = Queue()

# put items at the end of the queue
for x in range(4):
    q.put("item-" + str(x))

print(q.__dict__)
# remove items from the head of the queue
while not q.empty():
    print(q.get())
