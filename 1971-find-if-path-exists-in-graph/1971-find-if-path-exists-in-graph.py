class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = [[] for _ in range(n)]
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [0]*n
        stack = [source]
        visited[source] = 1
        while stack:
            node = stack.pop()
            if node == destination:
                return True

            for neigh in graph[node]:
                if visited[neigh] == 0: 
                    stack.append(neigh)
                    visited[neigh] = 1
        return False


        
        
        