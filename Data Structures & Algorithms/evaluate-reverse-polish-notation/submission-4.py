class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        val = 0
        for token in tokens:
            if token == '+':
                val = stack.pop() + stack.pop()
                stack.append(val)
            elif token == '-':
                b = stack.pop()
                a = stack.pop()
                val = a - b
                stack.append(val)
            elif token == '*':
                val = stack.pop() * stack.pop()
                stack.append(val)
            elif token == '/':
                b = stack.pop()
                a = stack.pop()
                val = a/b
                stack.append(int(val))
            else:
                stack.append(int(token))
        
        return stack[0]