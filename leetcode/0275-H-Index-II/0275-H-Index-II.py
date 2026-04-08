class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l = 0
        n = len(citations)
        r = n - 1
        ans = 0

        while l <= r:
            m = (l + r) // 2
            
            if citations[m] >= n - m:
                ans = n - m
                r = m - 1   
            else:
                l = m + 1  

        return ans