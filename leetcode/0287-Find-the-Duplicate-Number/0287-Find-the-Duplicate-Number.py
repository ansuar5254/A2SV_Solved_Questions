class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = 0
        slow = 0

        for _ in range(len(nums)):
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                print(slow)
                break
        slow1 = 0
        while True:
            slow = nums[slow]
            slow1 = nums[slow1]
            if slow == slow1:
                return slow