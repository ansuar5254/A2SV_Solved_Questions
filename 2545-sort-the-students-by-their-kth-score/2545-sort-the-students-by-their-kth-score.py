class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        sort_matrix = []
        check = []
        for i in range(len(score)):
            check.append([score[i][k],i])

        check.sort(reverse = True)
        for val,r in check:
            temp = []
            for i in range(len(score[r])):
                temp.append(score[r][i])

            sort_matrix.append(temp)
        return sort_matrix






        