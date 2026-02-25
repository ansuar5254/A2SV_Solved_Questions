from collections import defaultdict
def Phoenix_and_Socks():
    n,l,r = map(int,input().split())
    a = list(map(int,input().split()))
    left = defaultdict(int)
    right = defaultdict(int)
    for i in range(n):
        if i < l:
           left[a[i]] += 1 
        else:
           right[a[i]] += 1
    
    dollar = 0
    
    for key,value in left.items():
        if key in right and right[key] > 0:
            m = min(value,right[key])
            left[key] -= m
            right[key] -= m
            if right[key] == 0:
                del right[key]
    
        

    left_num = 0 
    right_num  = 0
    for value in left.values():
        left_num += value 
   

    for value in right.values():
        right_num += value 
 

    if left_num <= right_num:
        left_nums = []
        for key,val in left.items():
            for _ in range(val):
                left_nums.append(key)
        
        odds = []
        evens = []
        for key,value in right.items():
            if value == 0:
                continue
            if value % 2:
                odds.append([key,value])
            else:
                evens.append([key,value])


        for _ in left_nums:
            if odds:
                x,y = odds.pop()
                right[x] -= 1

                if y-1 != 0:
                    evens.append([x,y-1])
                dollar += 1
            else:
                x,y = evens.pop()
                right[x] -= 1
                odds.append([x,y-1])
                dollar += 1
                
        for key,value in right.items():
            if value > 0:
                if value >= 1:
                    if value % 2 == 0:
                       dollar += (value//2)
                    else:
                        dollar += ((value//2) + 1)
                
                

    else:
        right_nums = []
        for key,val in right.items():
            for _ in range(val):
                right_nums.append(key)
        
        
        odds = []
        evens = []
        for key,value in left.items():
            if value == 0:
                continue
            if value % 2:
                odds.append([key,value])
            else:
                evens.append([key,value])


        for _ in right_nums:
            if odds:
                x,y = odds.pop()
                left[x] -= 1

                if y-1 != 0:
                    evens.append([x,y-1])
                dollar += 1
            else:
                x,y = evens.pop()
                left[x] -= 1
                odds.append([x,y-1])
                dollar += 1
    

        for key,value in left.items():
            if value > 0:
                if value > 1:
                    if value % 2 == 0:
                        dollar += (value//2)
                    else:
                        dollar += ((value//2) + 1)
                else:
                    dollar += 1
           
    
    return dollar
    
t = int(input())
for _ in range(t):
    print(Phoenix_and_Socks())
