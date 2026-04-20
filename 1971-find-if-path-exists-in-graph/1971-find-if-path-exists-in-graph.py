class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = [[] for _ in range(n)]
        visited = [0]*n
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs (node):
            if node == destination:
                return True
            
            visited[node] = 1
            
            for neigh in graph[node]:

                if visited[neigh] == 0:
                    found = dfs(neigh)
                    if found:
                        return True

        f = dfs(source)
        if f:
            return True
        return False

        
        


     

