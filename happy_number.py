class Solution:
    def isHappy(self, n: int) -> bool:
        square_sum = set()
        while n != 1:
            n_copy = n
            s_sum = 0
            while n_copy > 0:
                    s_sum += (n_copy % 10) ** 2
                    n_copy //= 10
                    print(s_sum)
            n = s_sum
            if n in square_sum:
                return False
            else:
                square_sum.add(n)
        return True
            

                







        

        



        
