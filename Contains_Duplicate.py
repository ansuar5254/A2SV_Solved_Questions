class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicat_chek = set()
        for num in nums:
            if num in duplicat_chek:
                return True
            duplicat_chek.add(num)
        return False
