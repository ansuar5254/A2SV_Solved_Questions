"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        sub = defaultdict(list)
        imp = defaultdict(int)
      
        for e in employees:
            imp[e.id]= e.importance
            sub[e.id] = e.subordinates

        def dfs(node):
            total = imp[node]
            for neigh in sub[node]:
                total += dfs(neigh)

            return total

        return dfs(id)