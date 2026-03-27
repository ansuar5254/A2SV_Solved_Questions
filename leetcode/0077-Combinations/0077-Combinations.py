class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def helper(start,curr):
            if len(curr) == k:
                ans.append(curr[:])
                return 

            for i in range(start,n+1):
                curr.append(i)
                helper(i+1,curr)
                curr.pop()

    
        helper(1,[])
        return ans