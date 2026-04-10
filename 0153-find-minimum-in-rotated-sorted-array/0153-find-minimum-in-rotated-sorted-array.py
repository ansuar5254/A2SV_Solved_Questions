class Solution:
    def findMin(self, nums: List[int]) -> int:
        m =len(nums)-1
        low,high = 0,m
        while low < high:
            mid = (low + high)//2
            if nums[mid] > nums[high]:
                low = mid + 1

            else:
                high = mid

        return nums[high]