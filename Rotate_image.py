class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        for r in range(row):
            for c in range(r+1,row):
                matrix[r][c],matrix[c][r] = matrix[c][r],matrix[r][c]
        for r in range(row):
            matrix[r].reverse()
        return matrix


             
                

    
       



            


        
