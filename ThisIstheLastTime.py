def This_is_the_last_Time():    
        
        n,k = map(int,input().split())
        arr = [list(map(int,input().split())) for i in range(n)]

        arr.sort()
        for i in range(len(arr)):
               l,r,ki = arr[i]
               if l <= k <= r:
                      k = max(k,ki)
        return k

t = int(input())
for _ in range(t):
     print(This_is_the_last_Time())

        
            
        
