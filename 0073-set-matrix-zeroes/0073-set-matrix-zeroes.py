class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_row = set()
        zero_col = set()
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    if r not in zero_row:
                        zero_row.add(r)
                    if c not in zero_col:
                        zero_col.add(c)
        
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if r in zero_row or c in zero_col:
                    matrix[r][c] = 0
        return matrix
        

