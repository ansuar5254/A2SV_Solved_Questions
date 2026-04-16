class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dup = -1
        miss = -1
        
        for num in nums:
            num = abs(num)
            if nums[num-1] <  0:
                dup = num
            else:
                nums[num-1 ] *= -1



        for i in range(len(nums)):
            if nums[i] > 0:
                miss = i + 1

        return [dup,miss]
        

        
                
        

        

        


        
                

        
        