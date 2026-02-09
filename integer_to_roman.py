class Solution:
    def intToRoman(self, num: int) -> str:
        s = str(num)
        n = len(s)
        result = []
        mydict = {1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M',4:'IV',9:'IX',40:'XL',90:'XC',400:'CD',900:'CM'}
        for i in range(n):
            nu = int(s[i])*(10**(n-i-1))
            while nu > 0:
                if nu in mydict:
                    result.append(mydict[nu])
                    break
                elif nu < 5:
                    result.append('I')
                    nu -= 1
                elif nu < 10:
                    result.append('V')
                    nu -= 5
                elif nu < 50:
                    result.append('X')
                    nu -= 10 
                elif nu < 100:
                    result.append('L')
                    nu -= 50 
                elif nu < 500:
                    result.append('C')
                    nu -= 100
                elif nu < 1000:
                    result.append('D')
                    nu -= 500
                else:
                    result.append('M')
                    nu -= 1000
        return ''.join(result)
                  
                


            

            
        









        
