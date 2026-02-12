class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        sorted_s = sorted(count.items(),key = lambda x:-x[1])
        ans = []
        for key,value in sorted_s:
            ans.append(key*value)
        return ''.join(ans)
