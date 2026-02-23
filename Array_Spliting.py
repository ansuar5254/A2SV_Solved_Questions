def Array_Splitting():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    diff = []

    for i in range(1,n):
        diff.append(a[i]-a[i-1])
        
    diff.sort(reverse=True)
    return sum(diff[k-1:])

print(Array_Splitting())
