class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        count = Counter(nums)
        large = max(nums)
        while k > 1:
            while large in count:
                k -= 1
                count[large] -= 1
                if count[large] == 0:
                    del count[large]


                
            large -= 1
        return large
        
            
