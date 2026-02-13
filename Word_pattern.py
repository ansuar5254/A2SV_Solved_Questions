class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        n = len(pattern)
        m = len(s)
        pa_counter = Counter(pattern)
        s_count = Counter(s)
        maps = {}
        if n == m:
            for i in range(n):
                if pattern[i] not in maps:
                    maps[pattern[i]] = s[i]
            for i in range(n):
                if s_count[s[i]] != pa_counter[pattern[i]] or s[i] != maps[pattern[i]]:
                    return False
            return True
        else:
            return False
    

        
        
