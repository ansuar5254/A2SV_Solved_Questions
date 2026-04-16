class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        num = [0]*(len(nums) + 1)
        ans  = []
        for n in nums:
            num[n] += 1

        for i in range(1,len(nums)+1):
            if num[i] > 1:
                ans.append(i)
                break


        nums = set(nums)
        for i in range(1,len(num)):
            if i not in nums:
                ans.append(i)
                break
        return ans
                

        
        