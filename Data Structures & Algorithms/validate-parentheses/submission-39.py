class Solution:
    def isValid(self, s: str) -> bool:
        hm = { ")":"(", "]":"[", "}": "{" }
        st = []

        for ch in s:
            if ch == "(" or ch == "[" or ch == "{":
                st.append(ch)
            elif st and ch in hm and st[-1] == hm[ch]:
                st.pop()
            else:
                return False
        
        return False if st else True
