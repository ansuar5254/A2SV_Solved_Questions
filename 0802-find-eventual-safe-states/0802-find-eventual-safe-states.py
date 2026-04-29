class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        ans = []
        grey = 1
        black = 2
        order = []
        visited = [0]*len(graph)
        def dfs(node):
            if visited[node] == grey:
                return False

            if visited[node] == black:
                return True

            visited[node] = grey
            for neigh in graph[node]:
                if not dfs(neigh):
                    return False
            visited[node] = 2
            return True
        for i in range(len(graph)):
            if dfs(i):
                order.append(i)

        order.sort()
        return order