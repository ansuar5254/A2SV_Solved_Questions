class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        op = 0
        while target > 1 and maxDoubles != 0:
            if target % 2:
                op += 2
                target //= 2
            
            else:
                
                op += 1
                target //= 2
            maxDoubles -= 1
        if target > 1:
            op += (target-1)
        return op