class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {
            ")":"(",
            "}":"{",
            "]":"["
        }

        st = []

        for ch in s:
            if ch == "(" or ch == "[" or ch == "{":
                st.append(ch)
            elif st and ch in bracket_map and st[-1] == bracket_map[ch]:
                st.pop()
            else:
                return False
            
        return len(st) == 0