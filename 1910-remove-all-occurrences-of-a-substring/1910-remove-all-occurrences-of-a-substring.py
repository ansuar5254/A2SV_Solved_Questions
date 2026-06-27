class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        end_part = part[-1]
        for i in range(len(s)):
            flag = False
            if s[i] == end_part and len(stack) >= len(part)-1:
                print(stack)
                ind = -1
                for j in range(len(part)-2,-1,-1):
                    if part[j] != stack[ind]:
                        flag  = True
                        break
                    ind -= 1

                if not flag:
                    for _ in range(len(part)-1):
                        stack.pop()
                    
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])

        return ''.join(stack)







        