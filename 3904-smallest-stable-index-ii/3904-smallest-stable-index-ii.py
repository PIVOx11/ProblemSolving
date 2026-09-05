class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        l = len(nums)
        preMax = [0] * l
        sufMin = [nums[-1]] * l
        for i, v in enumerate(nums):
            if v > preMax[i - 1]:
                preMax[i] = v
            else:
                preMax[i] = preMax[i - 1]
        
        for i, v in zip(range(l-1, -1, -1), nums[::-1]):
            if i + 1 >= l:
                continue
            if nums[i] < sufMin[i + 1]:
                sufMin[i] = nums[i]
                continue
            sufMin[i] = sufMin[i + 1]
        # print(sufMin, preMax)
        for i in range(l):
            if preMax[i] - sufMin[i] <= k:
                return i           
        return -1