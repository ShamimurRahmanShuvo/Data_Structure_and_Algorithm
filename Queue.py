from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

if __name__ == '__main__':
    pq = Queue()
    pq.enqueue({
        'company' : 'Wal Mart',
        'timestamp' : '15 Apr, 11.01 AM',
        'price' : 131.10
    })
    pq.enqueue({
        'company' : 'Wal Mart',
        'timestamp' : '15 Apr, 11.05 AM',
        'price' : 132.30})
    pq.enqueue({
         'company': 'Wal Mart',
         'timestamp': '15 Apr, 11.10 AM',
         'price': 135
    })

    print(pq.buffer)
    print(pq.size())
    print(pq.dequeue())