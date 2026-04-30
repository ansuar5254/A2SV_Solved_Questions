from collections import deque
def solving():
    n = int(input())
    a = list(map(int,input().split()))
    indgree = [0]*(n+1)
    graph = [[] for _ in range(n+1)]
    for i in range(1, n+1):
        graph[i].append(a[i-1])
        indgree[a[i-1]] += 1
        
    q = deque()
    for i in range(1,n+1):
        if indgree[i] == 0:
            q.append(i)


    count = 0

    while q:
        for _ in range(len(q)):
            node = q.popleft()
            for neigh in graph[node]:
                indgree[neigh] -= 1
                if indgree[neigh] == 0:
                    q.append(neigh)
        count += 1

    return count + 2
t = int(input())
for _ in range(t):
    print(solving())