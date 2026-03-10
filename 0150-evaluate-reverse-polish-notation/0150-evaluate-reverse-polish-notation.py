class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for op in tokens:
            if op == '+':
                if len(stack) > 1:
                    x = stack.pop()
                    y = stack.pop()
                    stack.append(x+y)
            elif op == '-':
                if len(stack) > 1:
                    x = stack.pop()
                    y = stack.pop()
                    stack.append(y-x)
            elif op == '/':
                if len(stack) > 1:
                    x = stack.pop()
                    y = stack.pop()
                    stack.append(int(y/x))
            elif op == '*':
                if len(stack) > 1:
                    x = stack.pop()
                    y = stack.pop()
                    stack.append(x*y)
            else:
                stack.append(int(op))
        return stack[0]
        
