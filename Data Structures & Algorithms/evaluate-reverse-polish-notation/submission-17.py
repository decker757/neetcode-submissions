class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+", "-", "*", "/"]
        st = []
        res = 0
        
        for ch in tokens:
            if ch not in operators:
                st.append(int(ch))
            else:
                num1 = st.pop()
                num2 = st.pop()
                if ch == "+":
                    res = num1 + num2
                elif ch == "-":
                    res = num2 - num1
                elif ch == "*":
                    res = num1 * num2
                else:
                    res = int(num2 / num1)
                st.append(res)
        
        return st[0]