class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        hm = {")": "(", "]": "[", "}": "{"}

        for ch in s:
            if ch == "(" or ch == "[" or ch == "{":
                st.append(ch)
            elif ch in hm and st:
                if st.pop() != hm[ch]:
                    return False
            else:
                return False
        
        return True if len(st) == 0 else False