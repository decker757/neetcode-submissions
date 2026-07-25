class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            if ch == '(' or ch == '[' or ch == '{':
                stack.append(ch)
            
            if stack:
                if ch == ')':
                    if stack.pop() != '(':
                        return False
                elif ch == ']':
                    if stack.pop() != '[':
                        return False
                elif ch == '}':
                    if stack.pop() != '{':
                        return False
            else:
                return False
        
        if stack:
            return False
        return True