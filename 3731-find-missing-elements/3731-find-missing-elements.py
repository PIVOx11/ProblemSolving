class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = set(nums)
        return [i for i in range(nums[0]+1, nums[-1]) if i not in n]