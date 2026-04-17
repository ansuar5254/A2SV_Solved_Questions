class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        count = Counter(nums)
        large = max(nums)

        while True:
            if large in count:
                if k <= count[large]:
                    return large
                else:
                    k -= count[large]
            large -= 1