class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        n = len(s)
        result = [0]*n
        for index,value in enumerate(indices):
            result[value] = s[index]
        return ''.join(result)
        
