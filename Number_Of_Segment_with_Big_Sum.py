def Number_of_Segment_with():
    n,s = map(int,input().split())
    a = list(map(int,input().split()))
    l = 0
    curr_sum = 0
    num_good_sum = 0
    for r in range(n):
        curr_sum += a[r]
        while curr_sum >= s and l <= r:
            curr_sum -= a[l]
            l += 1
        if curr_sum <= s:
            num_good_sum += (r-l+1)
    n = (n*n + n)//2
    return n-num_good_sum
        
print(Number_of_Segment_with())

    
