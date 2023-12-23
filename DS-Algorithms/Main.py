from Stack import *
from Queue import *
from LinkedList import *


def switch_stacks(s1: Stack, s2: Stack):
    print("Stack1 and Stack2 Before Switching : ")
    print("S1:", s1.__str__())
    print("S2:", s2.__str__())

    tempQ = Queue(s1.max_length)
    list1 = []
    while (s1.top != -1):
        list1.append(s1.pop())
        if (len(list1) == s1.max_length):
            list1 = list1[::-1]
            for item in list1:
                tempQ.enqueue(item)

    list2 = []
    while (s2.top != -1):
        list2.append(s2.pop())
        if (len(list2) == s2.max_length):
            list2 = list2[::-1]
            for item in list2:
                if (not s1.is_full()):
                    s1.push(item)

    while (tempQ.current_size != 0):
        item = tempQ.dequeue()
        if (not s2.is_full()):
            s2.push(item)

    print("Stack1 and Stack2 After Switching : ")
    print("S1:", s1.__str__())
    print("S2:", s2.__str__())


if __name__ == '__main__':
    stack1 = Stack(2)
    stack1.push(2)
    stack1.push(3)
    stack2 = Stack(3)
    stack2.push(11)
    stack2.push(13)
    stack2.push(17)
    print("------------------------------------------")

    switch_stacks(stack1, stack2)
