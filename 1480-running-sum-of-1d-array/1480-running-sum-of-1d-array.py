class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        ans = []
        ans.append(nums[0])
        curr_sum = nums[0]
        for i in range(1,len(nums)):
            curr_sum += nums[i]
            ans.append(curr_sum)
        return ans
        