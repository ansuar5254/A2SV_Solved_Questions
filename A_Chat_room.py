from collections import Counter
s = input()
target = 'hello'
target = list(target)
l = 0 
r = len(s)-1
while l<=r:
    if target:
        if target and s[l] == target[0]:
            target.remove(target[0])
        if target and s[r] == target[-1]:
            target.pop()
        l += 1
        r -= 1
    else:
        print("YES")
        exit()
print("NO" if target else "YES")


    
