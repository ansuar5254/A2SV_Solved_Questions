class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def helper(i,curr):
            ans.append(curr[:])

            for j in range(i,len(nums)):
                curr.append(nums[j])
                helper(j+1,curr)
                curr.pop()
        helper(0,[])
        return ans