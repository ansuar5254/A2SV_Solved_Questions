class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        m = len(matrix[0])
        transpose = []
        for i in range(m):
            transpose.append([])
        k = 0
        for i in range(m):
            for j in range(n):
                transpose[i].append(matrix[j][i])
                
        return transpose


        
