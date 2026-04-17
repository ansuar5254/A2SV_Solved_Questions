class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[len(nums)-k]
        # l = 0
        # r = len(nums)-1
        # t = len(nums) - k
      
        # while l <= r:
        #     p = random.randint(l,r)
        #     w = l+1
           
        #     for i in range(w,r+1):
        #         if nums[i] < nums[p]: 
        #             nums[i],nums[w] = nums[w],nums[i]
        #             w += 1
            
        #     p = w-1
        #     nums[p],nums[l] = nums[l],nums[p]
        
        #     if  p == t:
        #         return nums[p]

        #     elif p < t:
        #         l = p+1
        #     else:
        #         r = p-1

             
