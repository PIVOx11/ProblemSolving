class Solution:
    def minMoves(self, nums: List[int]) -> int:
        target = max(nums)
        ans = 0
        for n in nums:
            ans += target - n

        return ans