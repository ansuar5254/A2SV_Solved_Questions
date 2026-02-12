class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        s = s1+s2
        count = Counter(s)
        unmathed = defaultdict(int)
        if count["x"]%2 != 0 or count["y"]%2 != 0:
            return -1
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                ss = s1[i]+s2[i]
                unmathed[ss] += 1

        min_swap = 0
        for val in unmathed.values():
            if val % 2 == 0:
                min_swap += val//2
            else: 
                one_swap = val//2
                min_swap +=(one_swap+1)
        return min_swap


        
        

        
        
        
      

    
        
                    

        


            
        
    

                    

            




        
