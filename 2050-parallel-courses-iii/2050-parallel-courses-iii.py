class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        n = n+1
        graph = [[] for _ in range(n)]
        indgree = [0]*n
        dist = [0]*n
        q = deque()
        for pre,course in relations:
            graph[pre].append(course)
            indgree[course] += 1

        for i in range(1,n):
            if indgree[i] == 0:
                q.append(i)
                dist[i] = time[i-1]

        while q:
            node =q.popleft()
            for neigh in graph[node]:
              
                dist[neigh] =max(dist[neigh],dist[node]+time[neigh-1])
                indgree[neigh] -= 1
                if indgree[neigh] == 0:
                    q.append(neigh)

        return max(dist)

        