from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        mydict = Counter(nums)
        count = 0
        for key,val in mydict.items():
            if val == 2:
                nums.append(key)
                count += 1
        n = len(nums)
        return nums[n-count:]
        

             
        
    

        
        
