class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        c1 = 0
        c2 = 0
        count1 = 0
        count2 = 0
        for num in nums:
            if num != c1 and num != c2 and count1 == 0:
                c1 = num
            elif num != c1 and num != c2 and count2 == 0:
                c2 = num
            
            if num == c1:
                count1 += 1
            elif num == c2:
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        countc1 = 0
        countc2 = 0
        for num in nums:
            if c1 == num:
                countc1 += 1
            elif c2 == num:
                countc2 += 1
        
        result  = []
        if countc1 > n//3:
            result.append(c1)
        if countc2 > n//3:
            result.append(c2)

        return result



        
