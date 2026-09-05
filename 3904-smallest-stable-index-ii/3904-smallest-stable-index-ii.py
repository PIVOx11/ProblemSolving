class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        l = len(nums)
        preMax = nums[0]
        sufMin = [0] * l
        mini = nums[-1]
        for i in range(l-1, -1, -1):
            if nums[i] < mini:
                mini = nums[i]
            sufMin[i] = mini
        print(sufMin)
        for i in range(l):
            if nums[i] > preMax:
                preMax = nums[i]
            if preMax - sufMin[i] <= k:
                return i           
        return -1