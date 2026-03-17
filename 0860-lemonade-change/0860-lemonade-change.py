class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        for i in range(len(bills)):
            change = bills[i]-5
            if change == 15:
                if five >= 1 and ten >= 1:
                    five -= 1
                    ten -= 1
                elif five >= 3:
                    five -=  3
                else:
                    return False
            if change == 10:
                if ten >= 1:
                    ten -= 1
                elif five >= 2:
                    five -= 2
                else:
                    return False
            if change == 5:
                if five >= 1:
                    five -= 1
                else:
                    return False
            if bills[i] == 5:
                five += 1

            elif bills[i] == 10:
                ten += 1
        return True
            

      


        
    

            

            
            
               