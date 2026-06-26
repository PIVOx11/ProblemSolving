class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i = 0
        result = []
        while i < len(nums):
            j = i + 1
            while j < len(nums):
                k = nums[i] + nums[j]
                k *= -1
                if k in nums:
                     res = sorted([nums[i], nums[j], nums[nums.index(k)]])
                     if res not in result and i != nums.index(k) and j != nums.index(k):
                        result.append(res)
                j += 1
            i += 1
        return result