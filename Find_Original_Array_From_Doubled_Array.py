class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        count = Counter(changed)
        
        ans = []
        #remove the number and it's double from dictionary
        for key in changed:
            if key in count and key*2 in count:
                ans.append(key)
                count[key] -= 1
                if count[key] == 0:
                    del count[key]
                count[key*2] -= 1
            
                if count[key*2] == 0:
                    del count[key*2]
            
        return [] if count else ans

        
        
            
            
            
            
        
        
        


    



      

            
                





        
