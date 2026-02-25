class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
    
        max_sum =sum(nums[:k])
        curr_sum = max_sum
        l = 0
        n = len(nums)
        for r in range(k,n):
            curr_sum -= nums[l]
            l += 1
            curr_sum += nums[r]
            max_sum = max(max_sum,curr_sum)
        return max_sum/k

