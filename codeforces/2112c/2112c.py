def coloringGame():
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    ans = 0
    for i in range(2,n):
        x = 0
        for j in range(i-1,0,-1):
            ax = max(a[-1],2*(a[i])) - a[i] - a[j]
            while x < j and a[x] <= ax:
                x += 1
            if j > x:
                ans += (j-x)
    return ans
t = int(input())
for _ in range(t):
    print(coloringGame())