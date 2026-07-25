class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opposites = {"}":"{", ")":"(", "]":"["}
        
        for ch in s:
            if ch == '}':
                if not stack or stack[-1] != opposites[ch]:
                    return False
                stack.pop()
            elif ch == ')':
                if not stack or stack[-1] != opposites[ch]:
                    return False
                stack.pop()
            elif ch == ']':
                if not stack or stack[-1] != opposites[ch]:
                    return False
                stack.pop()
            else:  
                stack.append(ch)
        
        return True if not stack else False