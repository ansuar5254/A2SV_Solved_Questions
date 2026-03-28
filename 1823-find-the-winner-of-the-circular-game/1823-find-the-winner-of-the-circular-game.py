class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = [i for i in range(1,n+1)]
        def helper(a):
            m = len(a)
            if m == 1:
                return a[0]

            a.remove(a[(k-1)%m])
            a = a[(k-1)%m:] + a[:(k-1)%m]
            print(a)
            return helper(a)
        return helper(arr)




        