class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def merge(left_arr,right_arr):
            l = 0
            r = 0
            ans = []
            while l < len(left_arr) and r < len(right_arr):
                if left_arr[l][0] <= right_arr[r][0]:
                    ans.append(left_arr[l])
                    l += 1
                else:
                    ans.append(right_arr[r])
                    r += 1

            ans.extend(left_arr[l:])
            ans.extend(right_arr[r:])
          
            return ans

        def divided(final,left,right):
            if left == right:
                return [[nums[left],left]]

            mid =( left+right)//2
            left_half = divided(final,left,mid)
            right_half = divided(final,mid+1,right)
            for a,b in left_half:
                ind = bisect.bisect_left(right_half,a,key = lambda x : x[0])
                final[b] += ind

            return merge(left_half,right_half)
        f = [0] * len(nums)
        divided(f,0,len(nums)-1)
        return f






                    
