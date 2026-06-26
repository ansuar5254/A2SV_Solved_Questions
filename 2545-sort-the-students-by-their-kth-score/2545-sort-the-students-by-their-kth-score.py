class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        sort_matrix = []
        check = []
        for i in range(len(score)):
            check.append([score[i][k],i])

        check.sort(reverse = True)
        for val,r in check:
            sort_matrix.append(score[r])
        return sort_matrix






        