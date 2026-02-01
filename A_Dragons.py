w = input().split()
s = int(w[0])
n = int(w[1])
sd = []
for i in range(n):
    d = input().split()
    x = int(d[0])
    y = int(d[1])
    sd.append((x,y))
sd.sort()
for sdr,bonus in sd:
    if s > sdr:
        s += bonus
    else:
        print("NO")
        exit()
print("YES")
    




 
