class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        ans = []
        for i in range(k):
            while q and q[-1] < nums[i]:
                q.pop()
            q.append(nums[i])

        ans.append(q[0])
        l = 0
        for i in range(k,len(nums)):
            if nums[l] == q[0]:
                q.popleft()
            while q and q[-1] < nums[i]:
                q.pop()
            q.append(nums[i])
            ans.append(q[0])
            l += 1
        return ans