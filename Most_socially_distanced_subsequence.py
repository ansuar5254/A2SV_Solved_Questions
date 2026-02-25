t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    aa = sorted(a)
    ans = []
    for i in range(n):
        if i == 0 or i == n-1 or (a[i-1]<a[i]) != (a[i] < a[i+1]):
            ans.append(a[i])

    print(len(ans))
    print(*ans)
        
