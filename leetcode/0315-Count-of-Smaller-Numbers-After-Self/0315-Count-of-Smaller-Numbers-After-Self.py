class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        count = [0] * len(nums)
        def merge(left_arr,right_arr):
            l ,r = 0,0
            merged = []
            while l < len(left_arr) and r < len(right_arr):
                if left_arr[l][0] <= right_arr[r][0]:
                    merged.append(left_arr[l])
                    l += 1
                else:
                    merged.append(right_arr[r])
                    r += 1

            merged.extend(right_arr[r:])
            merged.extend(left_arr[l:])
            return merged
        def divided(left,right):
            if left == right:
                return [[nums[left],left]]

            mid =( left + right)//2
            left_half = divided(left,mid)
            right_half = divided(mid+1,right)
            j = 0
            for i in range(len(left_half)):
                while j < len(right_half) and left_half[i][0] > right_half[j][0]:
                    j += 1
                count[left_half[i][1]] += j
                
            

            return merge(left_half,right_half)
        divided(0,len(nums)-1)
        return count