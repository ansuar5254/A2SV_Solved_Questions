n = int(input())
a = list(map(int,input().split()))
a.sort()
day = 0
for i in a:
    if day+1 <= i:
        day += 1 
print(day)
