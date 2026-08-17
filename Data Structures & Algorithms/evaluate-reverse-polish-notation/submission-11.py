class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = deque()
        ops = {"+", "-", "*", "/"}

        for ch in tokens:
            if ch not in ops:
                st.append(int(ch))
                continue
            else:
                operand1 = st.pop()
                operand2 = st.pop()

                if ch == "+":
                    st.append(operand1 + operand2)
                elif ch == "-":
                    st.append(operand2 - operand1)
                elif ch == '*':
                    st.append(operand1 * operand2)
                else:
                    st.append(int(float(operand2)/ operand1))

        return st[0]

                    
        