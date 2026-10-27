class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        operators = ["+", "*", "-", "/"]

        for t in tokens:
            if t in operators:
                op1 = int(st.pop())
                op2 = int(st.pop())

                if t == "+":
                    st.append(op1 + op2)
                elif t == "-":
                    st.append(op2 - op1)
                elif t == "*":
                    st.append(op1 * op2)
                elif t == "/":
                    st.append(int(op2 / op1))
            else:
                st.append(t)
                
        return int(st[0])