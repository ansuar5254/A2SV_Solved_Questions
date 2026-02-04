#User function Template for python3

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        from collections import defaultdict
        D_a = defaultdict(int)
        D_b = defaultdict(int)
        for i in a:
            D_a[i] += 1
        for i in b:
            D_b[i] += 1
        for k in D_b:
            if D_b[k] > D_a[k]:
                return False
        return True
            
      
        
       

    
    
    
    
