class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count_dict = {0:1}
        c = 0
        pre_sum = list(accumulate(nums))
        for i in range(len(pre_sum)):
            if pre_sum[i] % k in count_dict:
                c += count_dict[pre_sum[i]%k]
                count_dict[pre_sum[i] % k] += 1
            else:
                count_dict[pre_sum[i] % k] = 1
        return c