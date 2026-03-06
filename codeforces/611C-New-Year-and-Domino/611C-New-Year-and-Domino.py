h,w = map(int,input().split())
s = [list(input()) for _ in range(h)]
q = int(input())
que = [list(map(str,input().split())) for _ in range(q)]
pre_sum = [[0]*(w+1) for _ in range(h+1)]
ss = [[0]*w for _ in range(h)]

for i in range(h):
    for j in range(w):
        if s[i][j] =='.':
            if i+1 < h:
                if s[i+1][j] == '.':
                    ss[i][j] += 1
            if j+1 < w:
                if s[i][j+1] =='.':
                    ss[i][j] += 1
        
for i in range(len(pre_sum)-1):
    for j in range(len(pre_sum[0])-1):
        pre_sum[i+1][j+1] = ss[i][j] + pre_sum[i][j+1]+pre_sum[i+1][j] - pre_sum[i][j]

for i in range(q):
    r1,c1,r2,c2 = que[i]
    r1 = int(r1)
    r2 = int(r2)
    c1 = int(c1)
    c2 = int(c2)
    ans = pre_sum[r2][c2]-pre_sum[r1-1][c2]-pre_sum[r2][c1-1]+pre_sum[r1-1][c1-1]
    if c2 < w:
        for r in range(r1-1,r2):
            if s[r][c2-1] == '.' and s[r][c2] == '.':
                ans -= 1
    
    if r2 < h:
        for c in range(c1-1,c2):
            if s[r2-1][c] == '.' and s[r2][c] =='.':
                ans -= 1
    print(ans)