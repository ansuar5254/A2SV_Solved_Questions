
def blackAndWhite():
    n,k = map(int,input().split())
    s = input()
    countw = [0]
    for i in range(k):
        if s[i] == 'W':
            countw[0] += 1

    min_value = countw[0]
    l = 0
    for r in range(k,n):
        if s[r] == 'W':
            countw[0] += 1
        if s[l] == 'W':
            countw[0] -= 1
        l += 1 
        min_value = min(min_value,countw[0])
    return min_value
t = int(input())
for _ in range(t):
    print(blackAndWhite())
