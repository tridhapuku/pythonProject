# This file will contain implementation of queue using circular array

class CircularQueue():
    def __init__(self, len):
        self.length = len  # linmit of array
        self.size = 0  # will keep track the size of filled array

        # Init queue with none
        self.queue = [None for i in range(len)]
        self.front = self.rear = -1

    def enqueue(self, data):

        if self.size == self.length:
            print('Queue is full')
            return
        elif self.size == 0:
            self.front = self.rear = 0
            self.queue[self.rear] = data
            self.size = self.size + 1

        else:
            self.rear = (self.rear + 1) % self.length
            self.queue[self.rear] = data
            self.size = self.size + 1

    def dequeue(self):

        if self.size == 0:
            print('Queue is empty')
            return
        elif self.size == 1:
            temp = self.queue[self.front]
            self.front = self.rear = -1
            self.size = self.size - 1
        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.length
            self.size = self.size - 1

        return temp

    def display(self):
        countOfElems = 0
        indx = self.front
        while countOfElems < self.size:
            if indx >= self.length:
                indx = indx - self.length

            print('Queue Indx No {} , Count {} , Elem = {}'.format(indx, countOfElems,
                                                                   self.queue[indx]))
            countOfElems += 1
            indx = indx + 1


# Driver Code
ob = CircularQueue(5)
ob.enqueue(14)
ob.enqueue(22)
ob.enqueue(13)
ob.enqueue(-6)
ob.display()
print("Deleted value = ", ob.dequeue())
print("Deleted value = ", ob.dequeue())
ob.display()
ob.enqueue(9)
ob.enqueue(20)
ob.enqueue(5)
ob.display()
