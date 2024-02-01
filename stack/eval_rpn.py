from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {'+':'add', '-':'sub', '*':'mul', '/':'div'}

        for t in tokens:
            if t not in operations:
                stack.append(t)
            else:
                b = int(stack.pop())
                a = int(stack.pop())

                res = 0
                match t:
                    case '+':
                        res = a + b
                    case '-':
                        res = a - b
                    case '*':
                        res = a * b
                    case '/':
                        res = int(a / b)

                stack.append(res)

        return stack.pop()
    
Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])