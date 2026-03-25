class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = [i+1 for i in range(n)]
        def helper(a,m):
            if m == 1:
                return a[0]
            a.remove(a[(k-1)%m])
            a = a[(k-1)%m:] + a[:(k-1)%m]
            return helper(a,len(a))
        return helper(arr,n)