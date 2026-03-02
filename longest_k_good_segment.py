from collections import defaultdict
def longestKGoodSegment():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    count = defaultdict(int)
    ansl = 0
    ansr = 0
    l = 0
    max_len  = 0
    for r in range(n):
        count[a[r]] += 1
        while len(count) > k:
            count[a[l]] -= 1
            if count[a[l]] == 0:
                del count[a[l]]
            l += 1
        temp = max_len
        max_len = max(max_len,r-l+1)
        if max_len != temp:
            ansl = l+1
            ansr = r+1
    return [ansl,ansr]
print(*longestKGoodSegment())
            
        

    
