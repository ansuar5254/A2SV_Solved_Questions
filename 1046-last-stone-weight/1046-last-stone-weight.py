class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        def helper(stones):
            if len(stones) == 0:
                return 0
            if len(stones) == 1:
                return -stones[0]
            
            first = -heapq.heappop(stones)
            second = -heapq.heappop(stones)
            if first != second:
                heapq.heappush(stones,-(first-second))
                
            return helper(stones)

        return helper(stones)