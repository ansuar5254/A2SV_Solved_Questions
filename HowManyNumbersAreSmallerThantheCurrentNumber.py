class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        sortn = sorted(nums)
        for i in range(n):
            count = 0
            for j in range(n):
                if nums[i] > sortn[j]:
                    count += 1
                else:
                    break
            ans[i] = count
        return ans
