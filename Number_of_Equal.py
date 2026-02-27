from collections import Counter
def Number_of_Equal():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a =Counter(a)
    b = Counter(b)
    num_pair = 0
    for key,value in a.items():
        if key in b:
            num_pair += (value*b[key])
    return num_pair
print(Number_of_Equal())

    
