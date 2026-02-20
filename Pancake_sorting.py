class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
    
        f = max(arr)
        ans = []
        while f > 1:
            l = 0 
            r = arr.index(f)

            if r != 0:
               ans.append(r+1)

               while l < r:
                   arr[l],arr[r] = arr[r],arr[l]
                   l += 1
                   r -= 1

            l = 0
            ans.append(f)
            r = f-1

            while l < r:
                arr[l],arr[r] = arr[r],arr[l]
                l += 1
                r -= 1
            f -= 1
            
        return ans
        
