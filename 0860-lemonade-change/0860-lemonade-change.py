class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        pre_sum = 0
        change = defaultdict(int)
        for i in range(len(bills)):
            chan = bills[i] - 5
            if chan and chan in change:
                change[chan] -= 1
                if change[chan] == 0:
                    del change[chan]
            elif chan == 15 and 10 in change and 5 in change:
                change[10] -= 1
                if change[10] == 0:
                    del change[10]
                change[5] -= 1
                if change[5] == 0:
                    del change[5]

            elif chan == 15 and 5 in change and change[5] >= 3:
                change[5] -= 3
                if change[5] == 0:
                    del change[5]

            elif chan == 10 and 5 in change and change[5] >= 2:
                change[5] -= 2
                if change[5] == 0:
                    del change[5]
            elif chan != 0:
                return False

            change[bills[i]] += 1

        return True

        
    

            

            
            
               