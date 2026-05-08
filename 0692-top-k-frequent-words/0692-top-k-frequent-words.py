class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        
        ans = []
        heap = []
        for wo,fre in count.items():
            heapq.heappush(heap,(-fre,wo))

        for _ in range(k):
            fre,wo = heapq.heappop(heap)
            ans.append(wo)

        return ans
     