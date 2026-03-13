class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        mon_inc = deque()
        mon_dec = deque()
        longest = 0
        l = 0
        for i in range(len(nums)):
            while mon_inc and mon_inc[-1] > nums[i]:
                mon_inc.pop()
            
            while mon_dec and mon_dec[-1] < nums[i]:
                mon_dec.pop()

            mon_inc.append(nums[i])
            mon_dec.append(nums[i])
            while mon_dec and mon_inc and mon_dec[0] - mon_inc[0] > limit:
                x = mon_dec[0]
                y = mon_inc[0]
                if nums[l] == x:
                    mon_dec.popleft()
                if nums[l] == y:
                    mon_inc.popleft()
                l += 1
            longest = max(longest,i-l+1)
        return longest