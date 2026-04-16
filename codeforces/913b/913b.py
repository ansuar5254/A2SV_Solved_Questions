def christmas():
    n = int(input())
    a = []
    for _ in range(n-1):
        p = int(input())
        a.append(p)
    children = [[] for _ in range(n+1)]
    j = 2
    for p in a:
        children[p].append(j)
        j += 1

    for i in range(1,len(children)):
        if len(children[i]) > 0:
            leafcount = 0
            for child in children[i]:
                if len(children[child]) == 0:
                    leafcount += 1

            if leafcount < 3:

                return 'No'
            
    return 'Yes'

print(christmas())