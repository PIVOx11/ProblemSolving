class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if 0 not in nums:
            return len(nums) - 1
        if 1 not in nums:
            return 0

        l, r = 0, 0
        zeros = 0
        ans = 0
        while r < len(nums):
            if nums[r] == 0:
                zeros += 1
            if zeros < 2:
                ans = max(ans, r - l)
            else:
                zeros = zeros if nums[l] == 1 else zeros - 1
                l += 1
            r += 1

        return ans
