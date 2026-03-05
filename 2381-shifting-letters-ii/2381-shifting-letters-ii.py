class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        sh = [0]*n
        for shif in shifts:
            l,r,k = shif
            if k == 0:
                sh[l] -= 1
                if r < n-1:
                    sh[r+1] += 1
            else:
                sh[l] += 1
                if r < n-1:
                    sh[r+1] -= 1
        for i in range(1,n):
            sh[i] += sh[i-1]

        pos = []
        for i in s:
            pos.append(ord(i)-ord('a'))
        for i in range(len(pos)):
            pos[i] = chr(((pos[i]+sh[i])%26) + ord('a'))
        return ''.join(pos)

        
         

       
    