from collections import defaultdict, deque
import sys
input = sys.stdin.readline
def fox():
    n = int(input())
    grid = [input().strip() for _ in range(n)]
    graph = defaultdict(list)
    ans = []
    a = ord('a')
    indgree = [0]*26
    for i in range(n-1):
        m = min(len(grid[i]),len(grid[i+1]))
        flag = False
        for j in range(m):
            if grid[i][j] != grid[i+1][j]:
                u = ord(grid[i+1][j])-a
                graph[grid[i][j]].append(grid[i+1][j])
                indgree[u] += 1
                flag = True
                break
        if not flag and len(grid[i])>m:
            return 'Impossible'
   
    q = deque()
    for i in range(26):
        v = chr(a+i)
        if indgree[i]==0:
            q.append(v)
            ans.append(v)
    count = 0
    while q:
        node = q.popleft()
        for neigh in graph[node]:
                u = ord(neigh) - a
                indgree[u] -= 1
                if indgree[u] == 0:
                    ans.append(neigh)
                    q.append(neigh)
        
    if len(ans)!= 26:
        return 'Impossible'
    return ''.join(ans)


           
print(fox())