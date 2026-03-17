class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        rabit = 0
        for key,val in count.items():
            same_col = key+1
            groups = ceil(val/same_col)
            rabit += (groups*same_col)
        return rabit
            

            
