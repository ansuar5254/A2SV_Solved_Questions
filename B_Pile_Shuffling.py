t = int(input())
for i in range(t):
    n = int(input())
    operation = 0
    for j in range(n):
            a,b,c,d = map(int,input().split())
            if a>c:
                operation += a-c
                a = c
            if b > d:
                operation += (b-d) + a          
    print(operation)
                



        


