from Stack import *
from Queue import *

# Testing Stack Class
print("Testing Stack Class:")
my_stack1 = Stack(3)
my_stack2 = Stack(1)
my_stack3 = Stack(1)


my_stack1.push(1)
my_stack1.push(2)
my_stack1.push(3)
my_stack1.print_stack()
my_stack1.pop()
my_stack1.print_stack()


my_stack3.push(27)
print(my_stack3.is_full())
print(my_stack2.is_empty())

print("----------------------------------------------------------")

myqueue1 = Queue(6)
myqueue1.enqueue(27)
myqueue1.enqueue(45)
myqueue1.print_queue()
myqueue1.dequeue()
myqueue1.print_queue()
myqueue1.dequeue()


