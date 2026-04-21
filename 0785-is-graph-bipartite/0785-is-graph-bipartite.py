class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = [0]*len(graph)
        def dfs(node):
            for neigh in graph[node]:
                if not visited[neigh]:
                    if visited[node] == 1:
                        visited[neigh] = 2
                    else:
                        visited[neigh] = 1
                    if not dfs(neigh):
                        return False

                else:
                    if visited[neigh] == visited[node]:
                        return False 
            return True

        for i in range(len(graph)):
            if not visited[i]:
                visited[i] = 1
                if not dfs(i):
                    return False

        return True
        



                    
                    
                    
                    
            
            