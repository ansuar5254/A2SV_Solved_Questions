class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            num = str(num)
            for i in num:
                result.append(int(i))
        return result
            
        
