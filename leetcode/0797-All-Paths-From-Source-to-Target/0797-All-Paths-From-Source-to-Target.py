class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        ans = []
        def dfs(node,temp):
            nonlocal n
            if node == n-1:
                ans.append(temp[::])
                return

            for neigh in graph[node]:
                temp.append(neigh)
                dfs(neigh,temp)
                temp.pop()

            
        dfs(0,[0])
        return ans