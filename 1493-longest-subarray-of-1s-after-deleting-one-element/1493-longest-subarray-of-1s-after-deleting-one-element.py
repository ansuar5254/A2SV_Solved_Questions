class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = 0
        n = len(nums)
        num_zero = 0
        max_len = 0
        for r in range(n):
            if nums[r] == 0:
                num_zero += 1
            while  num_zero > 1:
                if nums[l] == 0:
                    num_zero -= 1
                l += 1
            max_len = max(max_len,r-l)
        return max_len
            
