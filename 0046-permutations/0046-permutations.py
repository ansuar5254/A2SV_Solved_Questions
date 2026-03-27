class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        visited = set()
        def helper(curr):
            if len(curr) == len(nums):
                ans.append(curr[:])
                return 

            for j in range(len(nums)):
                if nums[j] not in visited:
                    curr.append(nums[j])
                    visited.add(nums[j])
                    helper(curr)
                    curr.pop()
                    visited.remove(nums[j]) 
        helper([])
        return ans