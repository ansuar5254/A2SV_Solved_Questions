class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool: 
        n = len(graph)
        color = [0]*n
        red = 1
        blue = 2
        stack = []
        def dfs():
            while stack:
                node = stack.pop() 
                for neigh in graph[node]:
                    if color[neigh] == 0:
                        stack.append(neigh)
                        if color[node] == 1:
                            color[neigh] = 2

                        else:
                            color[neigh] = 1
                    else:
                        if color[node] == color[neigh]:
                            return False

            return True

        for i in range(len(graph)):
            if color[i] == 0:
                stack.append(i)
                color[i] = 1
                ans = dfs()
                if not ans:
                    return False
        

        return True
                
                




                

