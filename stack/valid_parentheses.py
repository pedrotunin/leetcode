class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            match c:
                case '}':
                    if self.top(stack) == '{':
                        stack.pop()
                        continue
                case ')':
                    if self.top(stack) == '(':
                        stack.pop()
                        continue
                case ']':
                    if self.top(stack) == '[':
                        stack.pop()
                        continue

            stack.append(c)

        return len(stack) == 0
    
    def top(self, s: list) -> str:
        if len(s) == 0:
            return ''
        return s[len(s) - 1]