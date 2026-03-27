class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        letter = {
            "2": "abc", "3": "def", "4": "ghi","5": "jkl", "6": "mno", "7": "pqrs","8": "tuv", "9": "wxyz"
        }
        
        ans = []
        def helper(i,curr):
        
            if i == len(digits):
                ans.append(curr)
                return 
        
            for ch in letter[digits[i]]: 
                helper(i+1,curr+ch)
        helper(0,'')
        return ans