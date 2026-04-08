class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(left_arr,right_arr):
            l = 0
            r = 0
            ans = []
            while l < len(left_arr) and r < len(right_arr):
                if left_arr[l] <= right_arr[r]:
                    ans.append(left_arr[l])
                    l += 1
                else:
                    ans.append(right_arr[r])
                    r += 1
            ans.extend(right_arr[r:])
            ans.extend(left_arr[l:])
            return ans
            
        def divided(left,right):
            if left == right:
                return [nums[left]]

            mid = (left+right)//2
            left_half = divided(left,mid)
            right_half = divided(mid+1,right)
            
            return merge(left_half,right_half)

        return divided(0,len(nums)-1)
            
        