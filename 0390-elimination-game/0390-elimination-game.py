class Solution:
    def lastRemaining(self, n: int) -> int:
        
        def helper(head,step,remain,left):
            if remain == 1:
                return head

            if left or remain % 2 :
                head += step

            return helper(head,step*2,remain//2,not left)

        return helper(1,1,n,True)
        
                
                

