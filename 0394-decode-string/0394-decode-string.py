class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        ans = []
        for i in range(len(s)):
            t = deque()
            while stack and s[i] == ']':
                x = stack.pop()
                if x != '[':
                    t.appendleft(x)
            
                else:
                    if stack:
                        x = stack.pop()

                        t = ''.join(t)
                
                        stack.append(t*int(x))
                        break
            if s[i] != ']':
                if s[i].isdigit() and stack and stack[-1].isdigit():
                    c = stack.pop()
                    stack.append(c+s[i])
                else: 
                    stack.append(s[i])
         
        return ''.join(stack)