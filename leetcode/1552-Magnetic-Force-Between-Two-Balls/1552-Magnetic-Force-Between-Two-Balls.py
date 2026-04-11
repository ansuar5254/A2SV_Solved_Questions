class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        self.ans = 0
        def checker(n):
            c = 1
            pre = position[0]
            for num in position[1:]:
                if num - pre >= n:
                    c += 1
                    pre = num
            if c >= m:
                return True

            else:
                return False

        def binar():
            low,high = 1,max(position)-min(position)

            while low <= high:
                mid = (low + high)//2
                if checker(mid):
                    self.ans = mid
                    low = mid + 1
                else:
                    high = mid - 1
        binar()
        return self.ans