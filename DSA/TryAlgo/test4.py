from typing import NoReturn, Dict, List

class Stack:
    def __init__(self):
        self.stack: List[int] = []
        self.incs: Dict[int, int] = {}

    def top(self) -> str:
        if not self.stack:
            return 'EMPTY'
        else:
            t = self.stack[-1] + self.incs.get(len(self.stack), 0)
            return str(t)

    def push(self, v: int) -> NoReturn:
        self.stack.append(v)

    def pop(self) -> NoReturn:
        stack_len = len(self.stack)
        v = self.incs.pop(stack_len, None)
        if v and stack_len > 1:
            self.inc(stack_len-1, v)

        self.stack.pop()

    def inc(self, i: int, v: int) -> NoReturn:
        self.incs[i] = v + self.incs.get(i, 0)


def superStack(operations):
    stack = Stack()
    list = []
    for operation in operations:
        parts = operation.split()

        if parts[0] == 'push':
            stack.push(int(parts[1]))
        elif parts[0] == 'inc':
            stack.inc(int(parts[1]), int(parts[2]))
        else:
            stack.pop()

        list.append(stack.top())
        # print(stack.top())
        # print(list)
        # print(stack.top())

    for i in range(len(list)):
        if list[i] != 'EMPTY':
            print(int(list[i]))
        else:
            print(list[i])
    return list


inp = ['push 4' , 'push 5' , 'inc 2 1', 'pop' , 'pop']

list2 = superStack(inp)
# print(superStack(inp))