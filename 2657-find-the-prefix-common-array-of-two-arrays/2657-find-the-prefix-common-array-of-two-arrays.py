class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        count = [0]*n
        ans = []
        comm = 0
        for i in range(n):
            count[A[i]-1] += 1
            if count[A[i]-1] == 2:
                comm += 1
            count[B[i]-1] += 1
            if count[B[i]-1] == 2:
                comm += 1
        
            ans.append(comm)
        return ans