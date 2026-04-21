class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        cities = 0
        stack = []
        graph = [[] for _ in range(n)]
        for r in range(n):
            for c in range(n):
                if isConnected[r][c] == 1:
                    graph[r].append(c)

     
            
        visited =[0]*n
        for node in range(n):
            if graph[node] and visited[node] == 0:
                stack.append(node)
             
                cities += 1
                visited[node] = 1
                while stack:
                    nod = stack.pop()
                    for neigh in graph[nod]:
                        if visited[neigh] == 0:
                            stack.append(neigh)
                            visited[neigh] = 1  
                                 
                      
        return cities


                                

                                

                   


