t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    if 'aa' in s:
        print(2)
    elif 'aba' in s:
        print(3)
    elif 'aca' in s:
        print(3)
    elif 'abca' in s:
        print(4)
    elif 'acba' in s:
        print(4)
    elif 'abbacca' in s or 'accabba' in s:
        print(7)
    else:
        print(-1)
