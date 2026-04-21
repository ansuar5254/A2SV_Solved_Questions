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
        visited = set()
        for e in employees:
            imp[e.id]= e.importance
            sub[e.id] = e.subordinates

        impo = 0

        def dfs(node):
            visited.add(node)
            nonlocal impo
            impo += imp[node]
            for neigh in sub[node]:
                if neigh not in visited:
                    dfs(neigh)

        dfs(id)
        return impo






            



     

        

        
            

      