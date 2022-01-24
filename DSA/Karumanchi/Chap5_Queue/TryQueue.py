# This file will contain linked list implementation of Queue

class Node:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        self.last = None

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data

    def setNext(self, next):
        self.next = next

    def getNext(self):
        return self.next

    def setlast(self, last):
        self.last = last

    def getLast(self):
        return self.last

    def hasNext(self):
        return (self.next != None)

class Queue:

    def __init__(self , data = None):
        self.front = None
        self.rear = None
        self.size = 0

    def enQueue(self , data):
        self.lastNode = self.front
        self.front = Node(data , self.front)
        
