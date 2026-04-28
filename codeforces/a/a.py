from collections import deque
import sys
input = sys.stdin.readline
def circ():
    n = int (input())
    graph = [[]*(n+1) for _ in range(n+1)]

    for _ in range(n-1):
        u,v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)

    q = deque()
    def bfs(start,n):
        q.append(start)
        visited = [-1]*(n+1)
        visited[start] = 0
        farthest = start
        while q:
            node = q.popleft()
            for neigh in graph[node]:
                if visited[neigh] == -1:
                    q.append(neigh)
                    visited[neigh]  = visited[node]+1
                    farthest = neigh
        return farthest,visited[farthest]
    if n == 1:
        return 0
    far_node, _ = bfs(1,n)
    _,diameter = bfs(far_node,n)
    return 3*diameter
print(circ())