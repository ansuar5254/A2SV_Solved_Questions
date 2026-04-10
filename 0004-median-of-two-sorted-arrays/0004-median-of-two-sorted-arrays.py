
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1

        n = len(nums1)
        m = len(nums2)
        t = m + n
        
        h = (t + 1) // 2   

        low, high = 0, n
        
        while low <= high:
            p1 = (low + high) // 2
            p2 = h - p1

            leftmax1 = float('-inf') if p1 == 0 else nums1[p1 - 1]
            rightmin1 = float('inf') if p1 == n else nums1[p1]

            leftmax2 = float('-inf') if p2 == 0 else nums2[p2 - 1]
            rightmin2 = float('inf') if p2 == m else nums2[p2]

            if leftmax2 <= rightmin1 and leftmax1 <= rightmin2:
                if t % 2:
                    return max(leftmax1, leftmax2)
                else:
                    return (max(leftmax1, leftmax2) + min(rightmin1, rightmin2)) / 2

            elif leftmax1 > rightmin2:
                high = p1 - 1
            else:
                low = p1 + 1