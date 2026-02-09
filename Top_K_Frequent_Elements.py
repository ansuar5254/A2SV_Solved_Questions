from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        count = sorted(count.items(),key = lambda x:-x[1])
        result = []
        for val,frq in count:
            result.append(val)
            k -= 1
            if k == 0:
                break
        return result
            
        
        
        
