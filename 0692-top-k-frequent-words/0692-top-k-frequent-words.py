class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        ss = sorted(count.items(),key = lambda x:(-x[1],x[0]))
        ans = []
        for i in range(k):
            ans.append(ss[i][0])

        return ans
     