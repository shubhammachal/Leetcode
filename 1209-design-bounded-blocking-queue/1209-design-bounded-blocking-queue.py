import threading
from collections import deque
class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.queue = deque() #stores the elements
        self.lock = threading.Lock() #lock for mutual exclusion
        self.not_full = threading.Condition(self.lock) #block enqueue if full
        self.not_empty = threading.Condition(self.lock) # block deque if empty
    def enqueue(self, element: int) -> None:
        with self.not_full: #acquire lock
            while len(self.queue) == self.capacity:
                self.not_full.wait() #block producer until space available

            self.queue.append(element) #append element
            self.not_empty.notify() #notify a consumer that the item is available
        

    def dequeue(self) -> int:
        with self.not_empty:
            while len(self.queue) == 0:
                self.not_empty.wait() #block consumer until item available
            val = self.queue.popleft()
            self.not_full.notify() #notify a waiting producer
        return val


        

    def size(self) -> int:
        with self.lock:
            return len(self.queue)
        