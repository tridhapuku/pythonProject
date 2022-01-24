# This file contains code for tree data structure
# Insert , PrintTree ,

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


# def insert(self , data):
def inorderTraversal(root):
    answer = []
    inorderTraversalUtil(root, answer)
    return answer


def inorderTraversalUtil(node, answer):
    if node is None:
        return
    # answer.append(node.data)
    inorderTraversalUtil(node.left, answer)
    answer.append(node.data)
    inorderTraversalUtil(node.right, answer)
    # answer.append(node.data)
    return


root = Node(1)

root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(inorderTraversal(root))
