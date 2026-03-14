class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for n in nums:
            i = abs(n)-1
            if nums[i] < 0:
                ans.append(abs(n))
            else:
                nums[i] = -nums[i]
        return ans

            
