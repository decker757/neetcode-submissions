class Solution:
    def decodeString(self, s: str) -> str:
        st = []

        for ch in s:
            if ch != "]":
                st.append(ch)
            else:
                subStr = ""
                while st[-1] != "[":
                    subStr = st.pop() + subStr
                st.pop()
                k = ""
                while st and st[-1].isdigit():
                    k = st.pop() + k
                st.append(int(k) * subStr)
        
        return "".join(st)