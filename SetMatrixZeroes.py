class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_row_col = defaultdict(set)
        n = len(matrix)
        for row in range(n):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    if row not in zero_row_col["r"]:
                        zero_row_col['r'].add(row)
                    if col not in zero_row_col['c']:
                        zero_row_col['c'].add(col)
        print(zero_row_col)
        for row in range(n):
            for col in range(len(matrix[0])):
                if row in zero_row_col['r'] or col in zero_row_col['c']:
                    matrix[row][col] = 0
        return matrix

        
        
