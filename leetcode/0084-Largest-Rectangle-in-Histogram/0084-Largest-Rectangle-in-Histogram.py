class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n  = len(heights)
        q = deque()
        max_area = 0
        r = 0
        l = 0
    
        for i in range(n):
            flag = True
            while q and heights[i] < q[-1][0]:
                x = q.pop()
                if flag:
                    l = x[1]
                    flag = False
                if q:
                 max_area = max(max_area,x[0]*(x[1]-q[-1][1])+(l-x[1])*x[0])
                
                else:
                    max_area = max(max_area,x[0]*(x[1]+1)+(l-x[1])*x[0])


            q.append([heights[i],i])

        l = 0
        while q:
            max_area = max(max_area,(n-l)*q[0][0])
            x,i = q.popleft()
            l = i+1
                
        return max_area