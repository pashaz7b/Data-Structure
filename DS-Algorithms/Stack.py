class Stack:
    def __init__(self, max_length):
        self.stack = []
        self.top = -1
        self.max_length = max_length

    def push(self, item):
        if (self.is_full()):
            raise Exception("Stack Is Full , Can't Add Item")

        else:
            self.top += 1
            self.stack.append(item)


    def pop(self):
        if (self.is_empty()):
            raise Exception("Stack Is Empty , Can't Delete Item")

        else:
            self.stack.pop(self.top)
            self.top -= 1


    def is_empty(self):
        if (self.top == -1):
            return True

        else:
            return False

    def is_full(self):
        if (self.top == self.max_length - 1):
            return True

        else:
            return False

    def print_stack(self):
        print(self.stack)
