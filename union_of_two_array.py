class Solution:    
    def findUnion(self, a, b):
        # code here
        arr = sorted(a+b)
        seen = [arr[0]]
        for i in arr[1:]:
            if i != seen[-1]:
                seen.append(i)
        return seen
