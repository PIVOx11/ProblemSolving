class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        l = len(nums)
        target = nums[l // 2]
        ans = 0
        for i in range(l):
            ans += abs(target - nums[i]) 
            i += 1
        return ans