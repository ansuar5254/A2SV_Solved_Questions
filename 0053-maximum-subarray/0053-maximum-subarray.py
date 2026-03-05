class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre = list(accumulate(nums))
        min_num = pre[0]
        max_whole = max(nums)
        max_num = max(min_num,max_whole)
        for i in range(1,len(pre)):
            if pre[i] >= min_num:
               max_num = max(max_num,pre[i]-min_num,pre[i])
            else:
                min_num = pre[i]
        return max_num


       
        


        
        


