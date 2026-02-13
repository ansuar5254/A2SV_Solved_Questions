class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        row = len(matrix)
        col = len(matrix[0])

        def first_row(r, c_end):
            for co in range(first_c, c_end + 1):
                ans.append(matrix[r][co])

        def last_col(r_end, c):
            for ro in range(first_r + 1, r_end + 1):
                ans.append(matrix[ro][c])

        def last_row(r, c_end):
            for co in range(c_end - 1, first_c - 1, -1):
                ans.append(matrix[r][co])

        def first_col(r_end, c):
            for ro in range(r_end - 1, first_r, -1):
                ans.append(matrix[ro][c])

        first_r = 0
        first_c = 0
        r = row - 1
        c = col - 1

        while first_r <= r and first_c <= c:
            first_row(first_r, c)
            last_col(r, c)
            if first_r < r:
                last_row(r, c)
            if first_c < c:
                first_col(r, first_c)     
            first_r += 1
            first_c += 1
            r -= 1
            c -= 1

        return ans
