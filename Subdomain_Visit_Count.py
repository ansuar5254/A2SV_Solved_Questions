class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        cpdDict = {}
        for i in range(len(cpdomains)):
            rep = 0
            l = 0
            n = len(cpdomains[i])
            r = n - 1
            while l<n:
                if cpdomains[i][l] == ' ':
                    rep = int(cpdomains[i][0:l])
                    l += 1 
                    print(rep)
                    break
                l += 1
            allDom = cpdomains[i][l:]
            print(allDom)
            if allDom in cpdDict:
                cpdDict[allDom] += rep
            else:
                cpdDict[allDom] = rep
            while  r >= l:
                if cpdomains[i][r] == '.':
                    if cpdomains[i][r+1:] in cpdDict:
                            cpdDict[cpdomains[i][r+1:]] += rep 
                    else:
                        cpdDict[cpdomains[i][r+1:]] = rep
                r -= 1
            
        result = []
        for key, value in cpdDict.items():
            result.append(str(value) + ' ' + key)
        return result
            
                
                    




                
                
             
                    


                


                


            






        
