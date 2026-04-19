class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = Counter(nums)
        i = 0
        arr = [0,1,2]
        for num in arr:
            if num in count:
                for _ in range(count[num]):
                    nums[i] = num
                    i += 1
            

        


        