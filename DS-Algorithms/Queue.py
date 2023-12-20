class Queue:
    def __init__(self, max_length):
        self.max_length = max_length
        self.queue = []
        self.front = -1
        self.rear = -1

    def enqueue(self, item):
        if (self.is_full()):
            raise Exception("Queue Is Full Can't Add Item")

        else:
            self.rear += 1
            self.queue.append(item)

    def dequeue(self):
        if (self.is_empty()):
            raise Exception("Queue Is Empty Can't Delete Item")

        else:
            self.front += 1
            self.queue.pop(self.front)

    def is_empty(self):
        if (self.rear == self.front):
            return True

        else:
            return False

    def is_full(self):
        if (self.rear == self.max_length - 1):
            return True

        else:
            return False

    def print_queue(self):
        print(self.queue)
