class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        n = len(nums)
        pre_sum = list(accumulate(nums))
        ans = min(pre_sum)
        max_value = max(pre_sum)
        return abs(ans)+1 if ans <= 0 else 1