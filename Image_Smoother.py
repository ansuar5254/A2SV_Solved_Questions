class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        n = len(img)
        m = len(img[0])
        result = []
        for r in range(n):
            temp = [0]*m
            result.append(temp)

        for r in range(n):
            for c in range(m):
                sum_cell = img[r][c]
                count = 1

                if r-1 >= 0:
                    sum_cell += img[r-1][c]
                    count += 1

                if r + 1 < n:
                    sum_cell += img[r+1][c]
                    count += 1

                if c-1 >= 0:
                    sum_cell += img[r][c-1]
                    count += 1

                if c + 1 < m:
                    sum_cell += img[r][c+1]
                    count += 1

                if r-1 >= 0 and c-1 >= 0:
                    sum_cell += img[r-1][c-1]
                    count += 1

                if r+1 < n and c+1 < m:
                    sum_cell += img[r+1][c+1]
                    count += 1
                
                if r+1 < n and c-1 >= 0:
                    sum_cell += img[r+1][c-1]
                    count += 1
                if c+1 < m and r-1 >= 0:
                    sum_cell += img[r-1][c+1]
                    count += 1

                result[r][c] = sum_cell//count
        return result

                



        

        
