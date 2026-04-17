class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] < 0:
                nums[i] = 1
            else:
                nums[i] += 1
        for num in nums:
            num = abs(num) - 2
            if 0 <= num < n and nums[num] > 0:
                nums[num] *= -1
        for i in range(1,n+1):
            if nums[i-1] > 0:
                return i
        return n + 1