from collections import defaultdict
def segmentsWithSmallSet():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    count = defaultdict(int)
    l = 0 
    num_good_sum = 0
    for r in range(n):
        count[a[r]] += 1
        while len(count) > k and l < n:
            count[a[l]] -= 1
            if count[a[l]] == 0:
                del count[a[l]]
            l += 1
        m = len(count)
        if m <= k:
            num_good_sum += (r-l+1)
    return num_good_sum 
print(segmentsWithSmallSet())


        
