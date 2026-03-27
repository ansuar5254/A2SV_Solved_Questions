class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        letter = {
            "2": "abc", "3": "def", "4": "ghi",
            "5": "jkl", "6": "mno", "7": "pqrs",
            "8": "tuv", "9": "wxyz"
        }
        ans = ['']
        for d in digits:
            temp = []
            for com in ans:
                for ch in letter[d]:
                    temp.append(com+ch)
            print(temp)
            ans = temp
        return ans

        
       