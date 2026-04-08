class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def validity(capa):
            used_day = 1
            ch = 0
            for w in weights:
                ch += w
                if ch > capa:
                    used_day += 1
                    ch = w 
                if used_day > days:
                    return False 
            return True 
                 
        l = max(weights)
        h = sum(weights)
        while l <= h:
            mid = (l+h)//2
            if validity(mid):
                ans = mid
                h = mid - 1
            else:
                l = mid + 1
                
        return l
        
        
                
            
                
                





        
        
            
        