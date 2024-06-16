class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == ']' and len(stack) and stack[-1] == '[':
                stack.pop()
            elif c == ')' and len(stack) and stack[-1] == '(':
                stack.pop()
            elif c == '}' and len(stack) and stack[-1] == '{':
                stack.pop()
            elif c in {'[','{','('}:
                stack.append(c)
            else:
                return False
        return len(stack) == 0
            
            

        