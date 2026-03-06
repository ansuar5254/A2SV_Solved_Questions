class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        before = [1]
        after = [1]
        accb = 1
        acca = 1
        r = n-1
        for i in range(n):
            accb *= nums[i]
            before.append(accb)
            if r >= 0:
               acca *= nums[r]
               after.append(acca)
            r -= 1

        after.reverse()
        before.append(1)
        after.insert(0,1)

        ans = []
        for i in range(n):
            ans.append(before[i]*after[i+2])
        return ans