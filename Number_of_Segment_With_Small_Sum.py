def Number_of_Segment_with():
    n,s = map(int,input().split())
    a = list(map(int,input().split()))
    l = 0
    curr_sum = 0
    max_value = 0
    for r in range(n):
        curr_sum += a[r]
        while curr_sum > s and l <= r:
            curr_sum -= a[l]
            l += 1
        if curr_sum <= s:
            max_value += (r-l+1)
    return max_value
        
print(Number_of_Segment_with())

    
