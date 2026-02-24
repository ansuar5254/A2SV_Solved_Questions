from collections import Counter
def Needle_in_a_Haystack():
    t = input()
    s = list(input())
    
    countt = Counter(t)
    s.sort()
    counts = Counter(s)

    for key,value in countt.items():
        if key not in counts:
            return 'Impossible'
        else:
            if value > counts[key]:
                return 'Impossible'
    l = 0
    ans = []
    while l < len(t):
        for key,value in counts.items():
            if key in countt:
                if t[l] == key:
                    ans.append(key)
                    counts[key] -= 1
                    countt[key] -= 1
                    break 
                else:
                    if counts[key]-countt[key] > 0:
                        ans.append(key*(counts[key]-countt[key]))
                        counts[key] -=(counts[key]-countt[key])
            else:
                if counts[key] > 0:
                    ans.append(key*counts[key])
                    counts[key]  = 0
        l += 1
    for key,value in counts.items():
        if value != 0:
            ans.append(key*value)
            
    return ''.join(ans)
n = int(input())
for _ in range(n):
    print(Needle_in_a_Haystack())
            
