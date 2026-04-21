class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = [0]*len(graph)
        stack = []

        for i in range(len(graph)):
            if not visited[i]:
                visited[i] = 1
                stack.append(i)
                while stack:
                    node = stack.pop()
                    for neigh in graph[node]:
                        if not visited[neigh]:
                            stack.append(neigh)
                            if visited[node] == 1:
                                visited[neigh] = 2
                            else:
                                visited[neigh] = 1
                        else:
                            print(node,visited[node],neigh,visited[neigh])
                            if visited[node] == visited[neigh]:
                                return False

        return True
                    


      

        



                    
                    
                    
                    
            
            