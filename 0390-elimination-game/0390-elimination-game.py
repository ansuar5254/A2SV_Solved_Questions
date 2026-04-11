class Solution:
    def lastRemaining(self, n: int) -> int:
        head = 1
        step = 1
        remain = n
        left = True
        while remain > 1:
            if left or remain % 2:
                head += step
           
            
            remain //= 2
            step *= 2
            left = not left
        return head
                
                

