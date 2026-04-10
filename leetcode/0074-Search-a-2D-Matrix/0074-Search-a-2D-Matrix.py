class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        low = 0
        high = n-1
        while low  <= high:
            mid = (low + high)//2
            l = 0
            h = len(matrix[mid])-1
            while l <= h:
                m = (l + h)//2
                if matrix[mid][m] == target:
                    return True

                elif matrix[mid][m] > target:
                    h = m -1

                else:
                    l = m + 1

            if l == 0:
                high = mid - 1
            elif h == len(matrix[mid])-1:
                low = mid + 1

            else:
                return False

        return False