class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack =[]
        min_val = nums[0]

        for i in range(1,len(nums)):
            while stack and nums[i] >= stack[-1][0]:
                stack.pop()
            if stack and nums[i] > stack[-1][1]:
                return True
            stack.append([nums[i],min_val])
            min_val = min(min_val,nums[i])
        
        return False