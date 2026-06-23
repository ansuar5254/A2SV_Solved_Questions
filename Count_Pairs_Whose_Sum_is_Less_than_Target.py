class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            t = target - nums[i]
            for j in range(i+1, n):
                if nums[j] < t:
                    ans += 1
        return ans     
