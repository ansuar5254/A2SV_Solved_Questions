class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        result = []
        even_sum = 0
        for num in nums:
            if num % 2 == 0:
                even_sum += num
        for val,ind in queries:
            if nums[ind] % 2 == 0:
                even_sum -= nums[ind]
            nums[ind] += val
            if nums[ind] % 2 == 0:
                even_sum += nums[ind]
            result.append(even_sum)
        return result

        
