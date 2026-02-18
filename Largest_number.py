class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(x) for x in nums]
        n = len(nums)
        for i in range(n):
            for j in range(1,n-i):
                if nums[j] + nums[j-1] > nums[j-1] + nums[j]:
                    nums[j],nums[j-1] = nums[j-1],nums[j]
         
        return ''.join(nums) if nums[0] != '0' else '0'
      
