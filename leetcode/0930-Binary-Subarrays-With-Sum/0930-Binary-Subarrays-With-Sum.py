class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        checker = {0:1}
        count = 0
        pre_sum = list(accumulate(nums))
        for num in pre_sum:
            if (num - goal) in checker:
                count += checker[num-goal]
            if num in checker:   
                 checker[num] += 1 
            else:
                checker[num] = 1

        return count