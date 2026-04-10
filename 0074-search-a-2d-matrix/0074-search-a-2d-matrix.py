class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low,high = 0,len(matrix)-1
        while low <= high:
            mid = (low + high)//2

            if matrix[mid][0] <= target <= matrix[mid][-1]:
                l = 0
                h = len(matrix[mid])-1
                while l <= h:
                    m = (l + h)//2
                    if matrix[mid][m] == target:
                        return True

                    elif matrix[mid][m] > target:
                        h = m - 1
                    else:
                        l = m + 1
                return False
            elif matrix[mid][0] > target:
                high = mid -1 
            
            else:
                low = mid + 1
        return False




        