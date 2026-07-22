class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # this is the iterative approach
        
        graph = [[] for _ in range(n)]

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        stack = [source]
        visited.add(source)
        while stack:
            node = stack.pop()
            if node == destination:
                return True
            for neigh in graph[node]:
                if neigh not in visited:
                   stack.append(neigh)
                   visited.add(neigh)

        return False
                   

    


        