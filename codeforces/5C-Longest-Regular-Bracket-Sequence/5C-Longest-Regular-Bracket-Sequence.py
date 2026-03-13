from collections import defaultdict
def longestRegularBracket():
    s = input()
    n = len(s)
    stack = []
    max_len = 0
    count = defaultdict(int)
    count[0] = 1
    addres = [0]*n
    for i in range(n):
        if s[i] == ')':
            if stack:
                x = stack.pop()
                if x-1 >= 0 and s[x-1] == ')' and addres[x-1] >= 0:
                    addres[i] = addres[x-1]
                    count[i-addres[x-1]+1] += 1
                else:
                    count[i-x+1] += 1
                    addres[i] = x
            else:
                addres[i] = -1
        else:
            stack.append(i)
            addres[i] = -1
    max_len = max(count)

    ans = [str(max_len),str(count[max_len])]
    return ans

print(*longestRegularBracket())