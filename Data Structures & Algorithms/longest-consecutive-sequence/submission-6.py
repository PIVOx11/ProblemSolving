class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        large = 0
        longest = 0
        for n in nums:
            if n - 1 not in nums:
                l = 0
                large = 0
                while n + l in nums:
                    large += 1
                    l += 1
                longest = large if large > longest else longest
        return longest
