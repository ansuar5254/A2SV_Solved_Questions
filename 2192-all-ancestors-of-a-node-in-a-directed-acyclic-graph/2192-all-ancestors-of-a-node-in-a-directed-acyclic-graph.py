class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = [[]*n for _ in range(n)]
        for u,v in edges:
            graph[v].append(u)
        
        ans = [0]*n
        def dfs(node,temp):
            stack = [node]
            visited = [0]*n
            visited[node] = 1
            while stack:
                nod = stack.pop()
                for neigh in graph[nod]:
                    if not visited[neigh]:
                        stack.append(neigh)
                        visited[neigh] = 1
                        temp.append(neigh)

            return temp 
        for i in range(n):
            temp = dfs(i,[])
            temp.sort()
            ans[i] = temp[::]

        return ans
        



                


            

