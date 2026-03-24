class Solution:
    def countGoodNumbers(self, n: int) -> int:
        odds = n//2
        evens = n-odds
        m = 10**9 + 7
        def helper(x,n):
            if n == 0:
                return 1
            half = helper(x,n//2)
            if n % 2:
                return (x * half * half) % m
            else:
                return (half * half) % m
        return (helper(5,evens)*helper(4,odds)) % m