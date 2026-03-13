class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        depth = 0
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(depth)
                depth = 0

            else:
                depth = stack.pop() + max(2*depth,1)
    
        return depth