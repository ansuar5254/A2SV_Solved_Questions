t = int(input())
for i in range(t):
    s = ''
    n = int(input())
    arr = list(map(str,input().split()))
    for j in range(len(arr)):
        if not s:
            s = arr[j]  
        elif s + arr[j] < arr[j]+s:
            s = s + arr[j]
        else:
            s = arr[j] + s 
    print(s)


    
    

   

    
    
