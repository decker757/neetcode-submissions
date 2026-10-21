class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_st = []
        t_st = []

        for ch in s:
            if ch != "#":
                s_st.append(ch)
            elif s_st and ch == "#":
                s_st.pop()
        
        for ch in t:
            if ch != "#":
                t_st.append(ch)
            elif t_st and ch == "#":
                t_st.pop()

        return s_st == t_st

