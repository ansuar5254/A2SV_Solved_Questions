class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l = 0 
        curr_sum = 0
        c1 = 0
        count = defaultdict(int)
        for r in range(n):
            count[nums[r]] += 1
            while len(count) > k:
                count[nums[l]] -= 1
                if count[nums[l]] == 0:
                    del count[nums[l]] 
                l += 1
            c1 += (r-l+1)
        
        l = 0 
        curr_sum = 0
        c2 = 0
        count = defaultdict(int)
        for r in range(n):
            count[nums[r]] += 1
            while len(count) >= k:
                count[nums[l]] -= 1
                if count[nums[l]] == 0:
                    del count[nums[l]] 
                l += 1
            c2 += (r-l+1)
        return c1 - c2


        

            


        

        

            
            