def flipTheBits():
    n = int(input())
    s1 = input()
    s2 = input()
    legal = []
    if s1 == s2:
        return 'YES'
    pre_sum = 0
    for i in range(n):
        pre_sum += int(s1[i])
        if i!=0 and (i+1) % 2 == 0 and pre_sum == (i+1)//2:
            legal.append(i)
    l = 0
    ans = 1
    flag = False

    if len(legal) == 0:
        return 'NO'
    
    for r in legal:
        if s1[l] == s2[l]:
            for i in range(l+1,r+1):
                if s1[i] != s2[i]:
                    ans = 0
                    flag = True
                    l = r+1
                    break
                
            if flag:
                break
        else:
            for i in range(l+1,r+1):
                if s1[i] == s2[i]:
                    ans = 0
                    flag = True
                    l = r+1
                    break
            if flag:
                break
        l = r+1
    if ans:
        for i in range(legal[-1]+1,n):
            if s1[i] != s2[i]:
                ans = 0
                break
    return 'YES' if ans else 'NO'
t = int(input())
for _ in range(t):
    print(flipTheBits())


