class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        index = {}
        for i in range(len(s)):
            index[s[i]] = i
        l = 0
        r = 0
        ans = []

        for i in range(len(s)):
            r = max(r,index[s[i]])

            if i == r:
                ans.append(r-l+1)
                l = r+1
    
        return ans
