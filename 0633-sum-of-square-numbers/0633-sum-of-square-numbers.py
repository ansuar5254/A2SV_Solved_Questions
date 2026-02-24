class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l = 0 
        r = int(sqrt(c)) 
        while l <= r:
            if l**2 + r**2 == c:
                return True
            elif l**2 + r**2 > c:
                r -= 1 
            else:
                l += 1
        return False
        