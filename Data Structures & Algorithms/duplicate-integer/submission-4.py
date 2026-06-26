class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check = set(nums)
        if len(nums) == len(check):
            return False
        return True