class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        operation = 0
        for i in range(n-2):
            if nums[i] == 0:
                operation += 1
                for j in range(i,i+3):
                    nums[j] = 1-nums[j]
        if len(set(nums))==1:
            return operation
        else:
            return -1