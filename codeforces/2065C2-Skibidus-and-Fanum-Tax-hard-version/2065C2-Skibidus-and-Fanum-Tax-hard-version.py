def find(num,right):
    low,high = 0,m-1
    ans = float('inf')
    while low <= high:
        mid = (low+high)//2
        if b[mid] - num <= right:
            ans = mid
            low = mid+1
    
        else:
            high = mid - 1
    return ans
    
def skibidus():
    if b[-1] - a[-1] > a[-1]:
        a[-1] = b[-1] - a[-1]

    right = a[-1]
    
    for i in range(n-2,-1,-1):
        bb = find(a[i],right)

    
        if a[i] <= right:
            if bb != float('inf'):
                right = max(a[i],b[bb]-a[i])
            else:
                right = a[i]
 
        else:
            if bb == float('inf'):
                return 'NO'
            else:
                right = b[bb] - a[i]
            
    return 'YES'

t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    b.sort()
    print(skibidus())