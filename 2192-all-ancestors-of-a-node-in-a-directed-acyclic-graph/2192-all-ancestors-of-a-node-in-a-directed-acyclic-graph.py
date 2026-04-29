class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(n)]
        indgree = [0]*n
        for u,v in edges:
            graph[u].append(v)
            indgree[v] += 1

        q = deque()
        ans = [set() for _ in range(n)]
        for i in range(n):
            if indgree[i] == 0:
                q.append(i)
              

        while q:
            node = q.popleft()
            for neigh in graph[node]:
                    ans[neigh] |= ans[node]
                    ans[neigh].add(node)
                    indgree[neigh] -= 1
                    if indgree[neigh] == 0:
                        q.append(neigh)

        return [sorted(list(s)) for s in ans]


        
                    


    
        
        



                


            

