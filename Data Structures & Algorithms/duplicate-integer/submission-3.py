class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        i = 0
        nums = sorted(nums)
        while i < len(nums) - 1:
            if nums[i] != nums[i + 1]:
                i += 1
                continue
            else:
                return True 
        return False