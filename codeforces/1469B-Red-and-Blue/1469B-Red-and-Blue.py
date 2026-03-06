from itertools import accumulate
def redAndBlue():
    n = int(input())
    a = list(map(int,input().split()))
    m = int(input())
    b = list(map(int,input().split()))

    #prefix sum for a
    max_pre_suma = max(0,max(list(accumulate(a))))

    #prefix sum for b
    max_pre_sumb = max(0,max(list(accumulate(b))))

    
    ans = max(0,max_pre_suma+max_pre_sumb)
    return ans

t = int(input())
for _ in range(t):
    print(redAndBlue())