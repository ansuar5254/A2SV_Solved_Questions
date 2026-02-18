class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        if mat == target:
            return True
        flag9 = True
        for r in range(n):
            for c in range(n):
                if mat[c][n-r-1] != target[r][c]:
                    flag9 = False
                    break
        if flag9:
            return True
        flag18 = True
        for r in range(n):
            for c in range(n):
                if mat[n-r-1][n-c-1] != target[r][c]:
                    flag18 = False
                    break
        if flag18:
            return True
        flag27 = True

        for r in range(n):
            for c in range(n):
                if mat[n-c-1][r] != target[r][c]:
                    flag27 = False
                    break
        if flag27:
            return True
        return False
