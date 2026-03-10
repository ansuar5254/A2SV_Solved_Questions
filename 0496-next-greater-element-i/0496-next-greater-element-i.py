class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}
        stack = []
        for i in range(len(nums2)):
            while stack and stack[-1] < nums2[i]:
                x = stack.pop()
                next_greater[x] = nums2[i]
            stack.append(nums2[i])
        ans =[]
        for i in range(len(nums1)):
            if nums1[i] in next_greater:
                ans.append(next_greater[nums1[i]])
            else:
                ans.append(-1)
        return ans
        
        
                