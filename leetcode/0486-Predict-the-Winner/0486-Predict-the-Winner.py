class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def helper(l,r):
            if l == r:
                return nums[r]
            
            r_cho = nums[r] - helper(l,r-1)
            l_cho = nums[l] - helper(l+1,r)

            return max(r_cho,l_cho)
        return helper(0,len(nums)-1) >= 0