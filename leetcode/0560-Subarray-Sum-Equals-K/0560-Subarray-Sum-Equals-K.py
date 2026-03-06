class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        checker = {0:1}
        count = 0
        pre_sum = list(accumulate(nums))
        for num in pre_sum:
            if (num - k) in checker:
                count += checker[num-k]
            if num in checker:   
                 checker[num] += 1 
            else:
                checker[num] = 1

        return count