class Solution:
    def myPow(self, x: float, n: int) -> float:
        flag = False
        if n < 0:
            return 1/self.myPow(x,-n)
        else:
            def helper(x,n):
                if n == 0:
                    return 1

                half = self.myPow(x,n//2)
        
                if n%2:
                    return half * half * x
                else:
                    return half * half
            return helper(x,n)
            
            
            
        
         
