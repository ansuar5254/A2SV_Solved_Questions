class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        pre_sum = list(accumulate(nums))
        inde = {0:-1}
        for i in range(len(pre_sum)):
            if pre_sum[i] % k in inde:
                if i - inde[pre_sum[i] % k] >= 2:
                    return True
            else:
                inde[pre_sum[i] % k] = i
        return False