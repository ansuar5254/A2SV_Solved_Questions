class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n = len(nums)
        right = nums[-1]
        num_rep = 0
        for i in range(n-2,-1,-1):
            left = nums[i]
            if left > right:
                c = ceil(left/right)
                num_rep += c-1
                right = left//c
            else:
                right = left
        return num_rep