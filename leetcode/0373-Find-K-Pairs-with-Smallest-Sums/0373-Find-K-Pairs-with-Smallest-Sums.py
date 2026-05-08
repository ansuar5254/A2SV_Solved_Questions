class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        heap = []
        ans = []
        for i in range(len(nums1)):
            heapq.heappush(heap,(nums1[i]+nums2[0],i,0))

        while k:
            val,i,j = heapq.heappop(heap) 
            k -= 1
            ans.append([nums1[i],nums2[j]]) 
            if j+1 < len(nums2):
                heapq.heappush(heap,(nums2[j+1]+nums1[i],i,j+1))
        return ans