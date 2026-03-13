class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        ans = [0]*n
        for i in range(n):
            while stack and temperatures[i] > stack[-1][0]:
                x = stack.pop()
                ans[x[1]] = i-x[1]
            
            stack.append([temperatures[i],i])
      
        return ans
        