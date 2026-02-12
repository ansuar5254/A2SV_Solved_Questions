class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        count = Counter(nums)
        n = len(nums)
        sorted_count = sorted(count.items(),key = lambda x:-x[1])
        max_fre= sorted_count[0][1]
        max_value = sorted_count[0][0]
        m = n - max_fre
        if max_fre - m <= 1:
            return -1
        count_max = 0
        count_other = 0
        for i in range(n):
            if nums[i] == max_value:
                count_max += 1
            else:
                count_other += 1
            if count_max - count_other == 1:
                return i
                


        

        
        




        
