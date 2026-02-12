class Solution:
    def findValidPair(self, s: str) -> str:
        count = Counter(s)
        l = 0
        for r in range(1,len(s)):
            if s[l]!= s[r]:
                if int(s[l]) == count[s[l]] and int(s[r]) == count[s[r]]:
                    return s[l]+s[r]
            l += 1
        return ''

        
        

        
