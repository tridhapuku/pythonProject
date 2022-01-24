
#This file will have Node as well as Operations

class Node:

    #Write init for SIngle Node creation
    def __init__(self, data, next):
        self.data =  data
        self.next = next

    def SetNext(self, next):
        self.next = next

def PrintList(head):
    tempNode =  head

    while tempNode != None:
        print(tempNode.data , end = ' -> ')
        tempNode = tempNode.next


def InsertNodeAfterK(head, data ,k):
    temp = head
    count = 0
    while temp!=None:
        count += 1
        if (count==k):
            newnode = Node(data, None)
            temp1 = temp.next
            temp.next = newnode
            newnode.next = temp1
            # count += 1
            break
        # count += 1
        temp = temp.next



#Test Operations

node1 = Node(4 , None)
node2 = Node(8 , None)
node3 = Node(12 , None)
node4 = Node(16, None)
node5 = Node(20, None)
node6 = Node(24, None)

node1.SetNext(node2)
node2.SetNext(node3)
node3.SetNext(node4)
node4.SetNext(node5)
node5.SetNext(node6)
node6.SetNext(None)

PrintList(node1)
InsertNodeAfterK(node1,5,6)
print()
PrintList(node1)

