class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        n = len(cards) + 1
        min_value = n
        myset = set()
        l = 0
        myset.add(cards[0])
        for r in range(1,len(cards)):
            if  cards[r] in myset:
                while cards[l]  != cards[r]:
                    myset.discard(cards[l])
                    l += 1

                min_value = min(min_value,r-l+1)
                myset.discard(cards[l])
                l += 1
            myset.add(cards[r])
        return min_value if min_value != n else -1
        
