# Single Linked list

class Node:

    # def __init__(self):
    #     self.data = None
    #     self.next = None

    def __init__(self, *args):
        if len(args) > 0:
            self.data = args[0]
        else:
            self.data = None
        self.next = None

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data

    def setNext(self, next):
        self.next = next

    def getNext(self):
        return self.next

    def hasNext(self):
        return self.next != None

class SLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        print('=' * 10)
        while printval is not None:
            print(printval.data)
            printval = printval.next

    def listLength(self):
        count = 0
        head = self.headval

        while head is not None:
            count += 1
            head = head.next
        return count
    
    def InsertAtBeginning(self , data):
        
        # Create temperary node
        tempNode = Node(data)
        # tempNode.data = data
        
        # tempHead = self.headval
        tempNode.next = self.headval
        self.headval = tempNode

    def InsertAtEnd(self , data):

        tempNode = Node(data)

        tempHead = self.headval

        if tempHead is None:
            self.headval = tempHead

        while tempHead is not None:

            if tempHead.next is None:
                tempHead.next = tempNode
                break
            tempHead = tempHead.next

    def DeleteFirstNode(self):
        tempHead = self.headval

        self.headval = tempHead.next

        del tempHead

    def DeleteLastNode(self):
        tempHead = self.headval

        if tempHead is None:
            print('Empty List')
            return

        if tempHead.next is None:
            self.headval = None
            return

        previousNode = tempHead
        # while tempHead.next is not None:
        #     previousNode = tempHead
        #     tempHead = tempHead.next

        while tempHead.next.next is not None:
            tempHead = tempHead.next

        tempHead.next = None
        # previousNode.next = None

    def DeleteGivenNode(self , data):
        currentNode = self.headval

        previousNode = currentNode

        if currentNode is None:
            print('Empty List')
            return

        if currentNode.data == data:
            self.headval = currentNode.next
            return

        flag = 0
        while currentNode.next is not None:
            previousNode = currentNode

            if currentNode.next.data == data:
                previousNode.next = currentNode.next.next
                flag = 1
                break
            currentNode = currentNode.next

        if flag == 0:
            print('Elem={} not found'.format(data))



#Test for Single Linked list
list = SLinkedList()

list.headval = Node()
list.headval.setData('Mon')

e2 = Node('Tues')
e3 = Node('Wed')
list.headval.setNext(e2)
e2.setNext(e3)

list.listprint()
print(list.listLength())

list.InsertAtBeginning('Sun')
list.listprint()

list.InsertAtEnd('Thurs')
list.listprint()

list.DeleteFirstNode()
list.listprint()
# list.DeleteFirstNode()
# list.listprint()
# list.DeleteFirstNode()
# list.listprint()
# list.DeleteFirstNode()
# list.listprint()

# list.DeleteLastNode()
# list.listprint()
# list.DeleteLastNode()
# list.listprint()
# list.DeleteLastNode()
# list.listprint()
# list.DeleteLastNode()
# list.listprint()

# list.DeleteLastNode()
# list.listprint()

list.DeleteGivenNode('Mon')
list.listprint()

list.DeleteGivenNode('Wed')
list.listprint()

list.DeleteGivenNode('Wed')
list.listprint()

list.DeleteGivenNode('Tues')
list.listprint()

list.DeleteGivenNode('Thurs')
list.listprint()

list.DeleteGivenNode('Thurs')
list.listprint()