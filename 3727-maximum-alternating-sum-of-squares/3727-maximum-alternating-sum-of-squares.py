class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = sorted([i ** 2 for i in nums])

        half = len(n) // 2

        return sum(n[half:]) - sum(n[:half])