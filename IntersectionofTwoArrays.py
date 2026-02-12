class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num_set1 =set(nums1)
        num_set2 = set(nums2)
        ans = []
        for num in num_set1:
            if num in num_set2:
                ans.append(num)
        return ans


    
