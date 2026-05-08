class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        n = len(matrix)
        for r in range(n):
            heapq.heappush(heap,(matrix[r][0],r,0))

        while k-1:
            val,r,c = heapq.heappop(heap)
            k -= 1
            if c+1 < n:
                heapq.heappush(heap,(matrix[r][c+1],r,c+1))

        return heap[0][0]

            
                    