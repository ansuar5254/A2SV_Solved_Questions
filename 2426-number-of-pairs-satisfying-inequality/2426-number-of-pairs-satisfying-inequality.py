class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        arr = []
        count = [0]
        n = len(nums1)
        for i in range(n):
            arr.append(nums1[i]-nums2[i])
        def merged(left_arr,right_arr):
            l = 0
            r = 0
            merge = []
            while l < len(left_arr) and r < len(right_arr):
                if left_arr[l] <= right_arr[r]:
                    merge.append(left_arr[l])
                    l += 1
                else:
                    merge.append(right_arr[r])
                    r += 1

            merge.extend(left_arr[l:])
            merge.extend(right_arr[r:])
            return merge

        def divided(l,r):
            if l == r:
                return [arr[l]]

            m = (l + r)//2
            left = divided(l,m)
            right = divided(m+1,r)
            for i in range(len(left)):
                val = left[i] - diff
                ind = bisect_left(right,val)
                ind = len(right)-ind
                count[0] += ind
            return merged(left,right)
        divided(0,len(arr)-1)
        return count[0]

            


