class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        result = []
        stack = []
        result = []
        s = '$'.join(source)
        n = len(s)
        l = 0
        while l < n:
            if l+1 < n and s[l]+s[l+1] == '//':
                l += 2
                r = l
                while r < n and s[r] != '$':
                    r += 1
                l = r
            elif l+1 < n and s[l] + s[l+1] =='/*':
                l += 2
                r = l
                while r+1 < n and s[r] + s[r+1] != '*/':
                    r += 1
                l = r+2
            else:
                result.append(s[l])
                l += 1
        result = ''.join(result)
        result = result.split('$')
        final = []
        for i in result:
            if i != '':
                final.append(i)
        return final


        

                

                


       







    
        

                

                

            



        
