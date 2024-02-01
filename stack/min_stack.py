from typing import List, Tuple

class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append((val, min(val, self.getMin())))
        
    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        val, _ = self.stack[-1]
        return val

    def getMin(self) -> int:
        if not self.stack:
            return 2e32

        _, minimo = self.stack[-1]
        return minimo

minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
minStack.getMin()
minStack.pop()
minStack.top()
minStack.getMin()