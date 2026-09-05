class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = len(nums) - 1
        while i < j :
            if nums[i] == val and nums[j] != val:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
                j -= 1
            elif nums[i] != val:
                i += 1
            if nums[j] == val:
                j -= 1
        i = 0
        while i < len(nums) and nums[i] != val:
            i += 1
        return i 