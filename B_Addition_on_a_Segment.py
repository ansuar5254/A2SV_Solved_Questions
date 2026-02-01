t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    max_value = max(arr)
    count = 0
    for i in arr:
       if i != 0:
           count += 1

    print(count-(n-max_value))