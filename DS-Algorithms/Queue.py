class Queue:
    def __init__(self, max_length):
        self.max_length = max_length
        self.queue = []
        self.front = None
        self.rear = None
        self.current_size = 0

    def enqueue(self, item):
        if (self.is_full()):
            raise Exception("Queue Is Full Can't Add Item")

        else:
            self.queue.append(item)

        if (self.front is None):
            self.front = self.rear = 0

        else:
            self.rear = self.current_size

        self.current_size += 1

    def dequeue(self):
        if (self.is_empty()):
            raise Exception("Queue Is Empty Can't Delete Item")

        else:
            res = self.queue.pop(0)
            self.current_size -= 1
            if (self.current_size == 0):
                self.front = self.rear = 0

            else:
                self.rear = self.current_size - 1

            return res


    def is_empty(self):
        return (bool_exp := self.current_size <= 0)


    def is_full(self):
        return (bool_exp := self.current_size >= self.max_length)


    def __str__(self):
        return self.queue

    def gt_current_size(self):
        return self.current_size


