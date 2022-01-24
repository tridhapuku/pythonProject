
# This file will contain linked list implementation of Queue
# Geeksforgeeks : https://www.geeksforgeeks.org/queue-linked-list-implementation/


class Node:
    def __init__(self , data):
        self.data = data
        self.next = None


class Queue:

    def __init__(self):
        self.front = self.rear = None

    def enQueue(self , data):
        tempNode = Node(data)
        if self.rear == None:
            self.front = self.rear = tempNode
        else:
            self.rear.next = tempNode
            self.rear = tempNode


    def deQueue(self):

        if self.front == None:
            print('Queue is empty')
            return
        else:
            tempNode = self.front

            self.front = tempNode.next

            if self.front == None:
                self.rear = None
            return tempNode

    def isEmpty(self):
        return self.front == None

#Test code for testing queue

if __name__ == '__main__':
    q = Queue()
    q.enQueue(10)

    print('\nQueue front ' + str(q.front.data))
    print('Queue rear ' + str(q.rear.data))

    q.enQueue(20)
    print('\nQueue front ' + str(q.front.data))
    print('Queue rear ' + str(q.rear.data))

    q.deQueue()
    q.deQueue()

    q.enQueue(30)
    q.enQueue(40)
    q.enQueue(50)
    q.deQueue()

    print('\nQueue front ' + str(q.front.data))
    print('Queue rear ' + str(q.rear.data))