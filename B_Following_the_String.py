from collections import Counter
testCase = int(input())
for te in range(testCase):
    result = []
    n = int(input())
    t = list(map(int, input().split()))
    mydict = {}
    y = 97
    for i in t:
            if i == 0:
                chara = chr(y)
                result.append(chara)
                mydict.get(chara,0) + 1
                y += 1
            else:
                 for cha,val in mydict:
                      if i == val-1:
                           result.append(cha)
                           mydict[cha] += 1
                           break
                        
                 
    result = ''.join(result)
    print(result)
            



    
    
    
        

 

