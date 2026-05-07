class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        n = len(piles)
        
        def heapdown(i,n):
            sw = i
            lc = i*2 + 1
            rc = i*2 + 2
            if lc < n and piles[lc] > piles[sw]:
                sw = lc

            if rc < n and piles[rc] > piles[sw]:
                sw = rc

            if i != sw:
                piles[sw],piles[i] = piles[i],piles[sw]
                heapdown(sw,n)

        for i in range(n//2-1,-1,-1):
            heapdown(i,n)

        while k:
            piles[0] = math.ceil((piles[0])/2)
            heapdown(0,n)
            k -= 1
       
        return sum(piles)

        

            
        

        