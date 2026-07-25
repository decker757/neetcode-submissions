class Solution:
    def isValid(self, s: str) -> bool:
        d = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }
        
        st = []
        for ch in s:
            if ch == '{' or ch == '(' or ch == '[':
                st.append(ch)
            else:
                if not st or st.pop() != d[ch]:
                    return False
        
        return len(st) == 0

        