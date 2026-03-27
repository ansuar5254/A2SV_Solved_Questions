class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def helper(start,curr):
            if len(curr) == k:
                ans.append(curr[:])
                return 

            if start > n:
                return

            curr.append(start)
            helper(start+1,curr)
            curr.pop()
            helper(start+1,curr)
        helper(1,[])
        return ans
        