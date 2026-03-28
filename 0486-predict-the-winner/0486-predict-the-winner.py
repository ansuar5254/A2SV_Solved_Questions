class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def helper(l,r):
            if l == r:
                return nums[l]
            l_cho = nums[l]-helper(l+1,r)
            r_cho = nums[r] - helper(l,r-1)

            return max(l_cho,r_cho)
        ans = helper(0,len(nums)-1)
        return True if ans>= 0 else False
        