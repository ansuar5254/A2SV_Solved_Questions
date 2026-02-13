class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ran_count = Counter(ransomNote)
        mag_count = Counter(magazine)
        for key,value in ran_count.items():
            if key not in mag_count or value > mag_count[key]:
                return False 
        return True
