

class Stack(object):

    def __init__(self , limit = 10):
        self.stack = []
        self.limit = limit

    def isEmpty(self):
        if len(self.stack) <= 0:
            return True
        else:
            return False

    def push(self, item):
        if len(self.stack) < self.limit:
            self.stack.append(item)
        else:
            print('Stack is full-- total {}'.format(self.limit))

    def pop(self):
        if len(self.stack) <= 0:
            print('Stack is empty')
        else:
            return self.stack.pop()

    def peek(self):
        if len(self.stack) <= 0:
            print('Stack is empty')
        else:
            return self.stack[-1]

    def size(self):
        return len(self.stack)


#Test for stack

our_stack = Stack(5)

our_stack.push('1')
our_stack.push('21')
our_stack.push('14')
our_stack.push("!")
our_stack.push("2 I")
our_stack.push("14")
our_stack.push("3J ")
our_stack. push(" 19")
our_stack.push("3")
our_stack. push("99")
our_stack.push("9")
print(our_stack.peek())
print(our_stack.pop())
print(our_stack.peek())
print(our_stack.pop())
print(our_stack.pop())
print(our_stack.pop())
print(our_stack.pop())
print(our_stack.pop())