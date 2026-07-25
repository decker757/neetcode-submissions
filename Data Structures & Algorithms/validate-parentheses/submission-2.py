class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opposites = {")" : "(", "}":"{", "]":"["}
        for ch in s:
            if ch in opposites:
                if stack and stack[-1] == opposites[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        return True if not stack else False
