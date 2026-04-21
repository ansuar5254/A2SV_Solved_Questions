class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for a,b in prerequisites:
            graph[b].append(a)

        visited = [0] * numCourses

        white = 0
        grey = 1
        black = 2

        def dfs(node):
            visited[node] = grey
            for neigh in graph[node]:
                if visited[neigh] == grey:
                    return False
                elif visited[neigh] == black:
                    continue
                else:
                    if not dfs(neigh):
                        return False

            visited[node] = black
            return True

        for i in range(numCourses):
                if visited[i] == white:
                    if not dfs(i):
                        return False
        return True
        


