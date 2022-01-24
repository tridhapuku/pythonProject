

class Node:
    def __init__(self, data ):
        self.data = data
        self.left = None
        self.right = None

def printLeafNodes( head):
    # currentNode = head

    if head == None:
        return

    # if head.left == None and head.right == None:
    #     print(head.data, end=" ")

    if head.left :
        printLeafNodes(head.left)

    if head.right:
        printLeafNodes(head.right)

    if head.left == None and head.right == None:
        print(head.data, end=" ")

def printLeafNodesRToL( head):

    if head == None:
        return

    if head.right :
        printLeafNodesRToL(head.right)

    if head.left:
        printLeafNodesRToL(head.left)

    if head.left == None and head.right == None:
        print(head.data , end= " ")



if __name__ == "__main__":

    # Let us create binary tree shown in
    # above diagram
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(8)
    root.right.left.left = Node(6)
    root.right.left.right = Node(7)
    root.right.right.left = Node(9)
    root.right.right.right = Node(10)

    # print leaf nodes of the given tree
    printLeafNodes(root)
    print()
    printLeafNodesRToL(root)