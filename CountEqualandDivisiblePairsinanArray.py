class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        index = {}
        count = 0
        for i in range(len(nums)):
            if nums[i] not in index:
                index[nums[i]] = []
            index[nums[i]].append(i)
        for key,value in index.items():
            for i in range(len(value)):
                for j in range(i+1,len(value)):
                    if (value[i]*value[j]) % k == 0:
                        count += 1
        return count 

       
 
                

        
