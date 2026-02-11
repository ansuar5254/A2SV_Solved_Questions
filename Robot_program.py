t = int(input())
for _ in range(t):
    n,x,k = map(int,input().split())
    s = input()
    capa = {}
    summ = 0
    for i in range(n):
        if s[i] == 'L':
            summ -= 1
        else:
            summ += 1
        if summ not in capa:
            capa[summ] = i
    count = 0
    if -x in capa:
        count = 1
        k -= (capa[-x]+1)
        if 0 in capa:
            count += (k//(capa[0]+1))
    print(count)



