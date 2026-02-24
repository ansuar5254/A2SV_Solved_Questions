class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_vol = 0 
        l = 0 
        r = len(height)-1
        while l < r:
            if height[l] <= height[r]:
                max_vol = max(max_vol,(height[l]*(r-l)))
                l += 1
            else:
                max_vol = max(max_vol,(height[r]*(r-l)))
                r -= 1
        return max_vol
