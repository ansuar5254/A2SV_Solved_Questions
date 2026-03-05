n,k,q = map(int,input().split())
rec = [list(map(int,input().split())) for _ in range(n+q)]
min_value = 200001
max_value = 0
for i in range(n+q):
    for j in range(2):
        min_value = min(min_value,rec[i][j])
        max_value = max(max_value,rec[i][j])

valid_che = [0]*(max_value-min_value+1)

for i in range(n):
    l,r = rec[i]
    valid_che[l-min_value] += 1
    if r < max_value:
        valid_che[(r-min_value)+1] -= 1

for i in range(1,len(valid_che)):
    valid_che[i] += valid_che[i-1]

for i in range(len(valid_che)):
    if valid_che[i] >= k:
        valid_che[i] = 1
    else:
        valid_che[i] = 0

for i in range(1,len(valid_che)):
    valid_che[i] += valid_che[i-1]
   
for i in range(n,n+q):
    l,r = rec[i]
    ans = 0 
    if l-min_value > 0:
        ans = valid_che[r-min_value] - valid_che[(l-min_value)-1]
    else:
        ans = valid_che[r-min_value]
    print(ans)