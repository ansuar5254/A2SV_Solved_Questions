class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexs = {}
        for i in range(len(nums)):
            if target - nums[i] in indexs:
                return [i,indexs[target - nums[i]]]
            indexs[nums[i]] = i
            
            



        

        
