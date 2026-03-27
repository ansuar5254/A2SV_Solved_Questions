class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letter = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",   
    "9": "wxyz"
}
        s = ''
        n = len(digits)
        ans = []
        if n == 1:
            s = letter[digits[0]]
            for i in range(len(s)):
                ans.append(s[i])
        elif n == 2:
            s1 = letter[digits[0]]
            s2 = letter[digits[1]]
            for i in range(len(s1)):
                for j in range(len(s2)):
                    ans.append(s1[i]+s2[j])
        elif  n == 3:
            s1 = letter[digits[0]]
            s2 = letter[digits[1]]
            s3 = letter[digits[2]]
            for i in range(len(s1)):
                for j in range(len(s2)):
                    for k in range(len(s3)):
                        ans.append(s1[i]+s2[j]+s3[k])
        else:
            s1 = letter[digits[0]]
            s2 = letter[digits[1]]
            s3 = letter[digits[2]]
            s4 = letter[digits[3]]
            for i in range(len(s1)):
                for j in range(len(s2)):
                    for k in range(len(s3)):
                        for m in range(len(s4)):
                            ans.append(s1[i]+s2[j]+s3[k]+s4[m])

        return ans
    


        

        

                


        