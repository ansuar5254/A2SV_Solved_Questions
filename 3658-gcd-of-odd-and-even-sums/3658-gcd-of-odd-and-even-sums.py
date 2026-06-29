class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        temp_o = 1
        temp_e = 2
        odd_sum = 0
        even_sum = 0
        for _ in range(n):
            odd_sum += temp_o
            even_sum += temp_e
            temp_e += 2
            temp_o += 2

        return math.gcd(odd_sum,even_sum)
