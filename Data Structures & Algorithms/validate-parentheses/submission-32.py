class Solution:
    def isValid(self, s: str) -> bool:
        hm = {")":"(", "]":"[", "}":"{"}
        st = []

        for ch in s:
            if ch == "[" or ch == "(" or ch == "{":
                st.append(ch)
            else:
                if not st or st.pop() != hm[ch]:
                    return False
        
        return True if len(st) == 0 else False
            
