class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]: 
        diagonal = defaultdict(list)
        row = len(mat)
        col = len(mat[0])
        for r in range(row):
            for c in range(col):
                 diagonal[r+c].append(mat[r][c])
        ans = []
        for key,value in diagonal.items():
            if key % 2 == 0:
                value.reverse()
                for val in value:
                    ans.append(val)
            else:
                for val in value:
                    ans.append(val)
        return ans
                

        
