class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        q = deque()
        n = len(temperatures)
        ans = []
        
        for i in range(n-1,-1,-1):
            count = 1
            if not q:
                ans.append(0)

            else:
                while q:
                    if temperatures[i] >= q[0][0]:
                        x,y = q.popleft()
                        count += y
                    else:
                        break
                if not q:
                    ans.append(0)
                else:
                    ans.append(count)
            q.appendleft([temperatures[i],count])
        ans.reverse()
        return ans
        
