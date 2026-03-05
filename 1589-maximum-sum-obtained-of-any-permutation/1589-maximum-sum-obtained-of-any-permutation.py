class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        pre_sum = [0]*n
        nums.sort()
        nums.reverse()
        total = 0
        for i in range(len(requests)):
            st,en = requests[i]
            pre_sum[st] += 1
            if en + 1 < n:
                pre_sum[en+1] -= 1
        pre_sum = list(accumulate(pre_sum))
        pre_sum.sort(reverse = True)

        for i in range(n):
            total += (pre_sum[i]*nums[i])
        return total % (10**9 + 7)

        
