def Broken_Keyboard():
    s = input()
    ans = set()
    l = 0
    n = len(s)
    r = 0
    while r < n:
        if r+1 < n and s[r+1] == s[l]:
            r += 1
        else:
            if (r-l+1) % 2 != 0:
                if s[l] not in ans:
                    ans.add(s[l])
            r += 1
            l = r
    ans = sorted(ans)
    return ''.join(ans)

t = int(input())
for _ in range(t):
    print(Broken_Keyboard())
