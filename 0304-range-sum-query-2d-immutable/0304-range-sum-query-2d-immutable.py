class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.pre_sum=[[0] * (len(matrix[0])+1) for _ in range(len(matrix)+1)]
    
        for r in range(len(self.pre_sum)-1):
            for c in range(len(self.pre_sum[0])-1):
                self.pre_sum[r+1][c+1]=matrix[r][c] + self.pre_sum[r][c+1] + self.pre_sum[r+1][c] - self.pre_sum[r][c]
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.pre_sum[row2+1][col2+1] - self.pre_sum[row1][col2+1] - self.pre_sum[row2+1][col1] + self.pre_sum[row1][col1] 
                