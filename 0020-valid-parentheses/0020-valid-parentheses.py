class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        def f(s, stack):
            for i in s:
                if len(stack) == 0:
                    if i == ')' or i == ']' or i == '}':
                        return False
                    else:
                        stack.append(i)
                else:
                    if stack[-1] == '(' and i == ')':
                        stack.pop()
                    elif stack[-1] == '[' and i == ']':
                        stack.pop()
                    elif stack[-1] == '{' and i == '}':
                        stack.pop()
                    else:
                        stack.append(i)
            
            if len(stack) == 0:
                return True
            else:
                return False
            
        return f(s, stack)