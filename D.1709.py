t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    k = 0
    result = []
    for i in range(n):
        for j in range(n-1-i):
            if a[j] > a[j+1]:
                k += 1
                a[j],a[j+1] = a[j+1],a[j]
                result.append([1,j+1])

    
    for i in range(n):
        for j in range(n-1-i):
            if b [j] > b[j+1]:
                k += 1
                b[j],b[j+1] = b[j+1],b[j]
                result.append([2,j+1])

    for i in range(n):
        if a[i] > b[i]:
            k += 1
            result.append([3,i+1])

    print(k)
    for i in range(len(result)):
        print(*result[i])

