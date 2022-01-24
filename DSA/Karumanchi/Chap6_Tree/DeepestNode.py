




class Node:

    def __init__(self , data ,left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def PrintTreePreOrder(self, node):

        if node is None:
            return
        print(node.data, end='->')
        self.PrintTreePreOrder(node.left)
        self.PrintTreePreOrder(node.right)

    def TraversalUsingQueue(self , node):

        que = []

        que.append(node)

        while len(que) > 0 :
            CurrentNode = que.pop(0)

            if CurrentNode.data is not None :
                print(CurrentNode.data, end= ' ')

            if CurrentNode.left :
                que.append(CurrentNode.left)

            if CurrentNode.right:
                que.append(CurrentNode.right)


    def TraversalUsingStack(self ,node):

        stack = []

        stack.append(node)

        while len(stack) > 0:
            CurrentNode = stack.pop()

            print(CurrentNode.data, end='->')
            if CurrentNode.right:
                stack.append(CurrentNode.right)

            if CurrentNode.left:
                stack.append(CurrentNode.left)

    def InorderUsingStack(self , node):

        stack = []
        current = node
        while 1:

            if current is not None:
                stack.append(current)
                current = current.left

            elif len(stack) > 0 :
                poppedNode = stack.pop()
                print(poppedNode.data, end='->')
                current = poppedNode.right
            else:
                break










# Tree

Root = Node(1, None, None)

NodeB = Node(2, None, None)
NodeC = Node(3)
NodeD = Node(4)
NodeE = Node(5)

Root.left = NodeB
Root.right = NodeC

NodeB.left = NodeD
NodeB.right = NodeE

Node6 = Node(6)
Node7 = Node(7)
Node8 = Node(8)
Node9 = Node(9)

NodeD.left = Node6
NodeD.right = Node7
NodeC.left = Node8
NodeC.right = Node9

# print(Root.PrintTreePreOrder(Root))
print(Root.TraversalUsingQueue(Root))
print(Root.TraversalUsingStack(Root))

print(Root.InorderUsingStack(Root))