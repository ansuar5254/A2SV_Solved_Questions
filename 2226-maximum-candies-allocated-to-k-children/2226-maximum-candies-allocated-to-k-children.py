class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:

        candies.sort()
        self.ans = 0

        def checker(n):
            c = 0
            for cand in candies:
                c += cand//n
        

            if c >= k:
                return True
            else:
                return False

        def binarySearch():
            low,high = 1,max(candies)
            while low <= high:
                mid = (low + high)//2
                if checker(mid):
                    print(mid)
                    self.ans = mid
                    low = mid + 1

                else:
                    high = mid - 1

        binarySearch()
        
        return self.ans 

                





        
        